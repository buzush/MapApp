from fabric.api import *
from fabric.contrib.files import upload_template, uncomment, append

APT_PACKAGES = [
    'unattended-upgrades',
    'ntp',

    'postgresql',
    'nginx',
    'supervisor',
    'python3',
    'virtualenvwrapper',
    'git',
    'python3-dev',
    'libpq-dev',
    'libjpeg-dev',
    'libjpeg8',
    'zlib1g-dev',
    'libfreetype6',
    'libfreetype6-dev',
    'postfix',
    'fail2ban',
    'postgis',
    'postgresql-9.3-postgis-2.1',
    'memcached',
    'libmemcached-dev',

    'htop',

    'rabbitmq-server',  # for offline tasks via celery

    'libxml2-dev',  # for lxml
    'libxslt1-dev',  # for lxml

    # # for numpy:
    # 'cython',
    # 'gfortran',
    # 'libblas-dev',
    # 'liblapack-dev',
    # 'python3-tz',
]


@task
def disable_ipv6():
    append('/etc/sysctl.conf', [
        'net.ipv6.conf.all.disable_ipv6 = 1',
        'net.ipv6.conf.default.disable_ipv6 = 1',
        'net.ipv6.conf.lo.disable_ipv6 = 1',
    ], use_sudo=True)
    run('sudo sysctl -p')


@task
def update_server_pkgs():
    run("sudo apt-get -qq update")
    run("sudo apt-get -q upgrade -y")


@task
def install_server_pkgs():
    update_server_pkgs()
    run("sudo apt-get -q install -y %s" % " ".join(APT_PACKAGES))


@task
def install_elasticsearch():
    run(
            'wget --no-check-certificate -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -')
    run(
            'echo "deb http://packages.elastic.co/elasticsearch/1.4/debian stable main" | sudo tee -a /etc/apt/sources.list')
    run("sudo apt-get -qq update")
    run("sudo apt-get -q upgrade -y")
    run("sudo apt-get -q install -y openjdk-7-jre elasticsearch")
    run("sudo update-rc.d elasticsearch defaults 95 10")
    run("sudo service elasticsearch start")  # Is this line needed?


@task
def install_elasticsearch_hebrew():
    # install plugin
    with cd("/usr/share/elasticsearch/"):
        run("sudo bin/plugin --install analysis-hebrew --url"
            " https://bintray.com/artifact/download/synhershko/"
            "elasticsearch-analysis-hebrew/elasticsearch-analysis-hebrew-1.7.zip")

    # get required hspell-data-files
    with cd("/usr/share/elasticsearch/plugins/analysis-hebrew/"):
        run(
                "sudo GIT_SSL_NO_VERIFY=true git clone https://github.com/nonZero/hspell-data-files.git ")

    # update configuration
    append(
            '/etc/elasticsearch/elasticsearch.yml',
            'hebrew.dict.path: /usr/share/elasticsearch/plugins/analysis-hebrew/hspell-data-files/',
            use_sudo=True,
    )
    sudo('service elasticsearch restart')


@task
def server_setup():
    disable_ipv6()
    install_server_pkgs()
    # install_elasticsearch()


@task
def host_type():
    run('uname -s')


@task
def hard_reload():
    run("sudo supervisorctl restart %s" % env.webuser)


@task
def very_hard_reload():
    run("sudo service supervisor stop")
    run("sudo service supervisor start")


@task
def log(n=50):
    run("tail -n{} {}*".format(n, env.log_dir))


@task
def nginx_log(n=50):
    run("tail -n{} /var/log/nginx/error.log".format(n))


@task
def create_webuser_and_db():
    run("sudo adduser %s --gecos '' --disabled-password" % env.webuser)
    run("sudo -iu postgres createuser %s -S -D -R" % env.webuser)
    run("sudo -iu postgres createdb %s -O %s" % (env.webuser, env.webuser))
    run("sudo -iu postgres psql -c \"alter user %s with password '%s';\"" % (
        env.webuser, env.webuser))
    enable_postgis(env.webuser)


@task
def create_biodb_normal_db():
    db = env.webuser + "_biodb"
    run("sudo -iu postgres createdb %s -O %s" % (db, env.webuser))
    enable_postgis(db)


@task
def enable_postgis(db=None):
    if db is None:
        db = env.webuser
    run(
            "sudo -iu postgres psql %s -c \"CREATE EXTENSION postgis;\"" % db)
    run(
            "sudo -iu postgres psql %s -c \"CREATE EXTENSION postgis_topology;\"" % db)


@task
def nginx_setup(secure=False):
    uncomment('/etc/nginx/nginx.conf',
              'server_names_hash_bucket_size\s+64',
              use_sudo=True)

    nginx_conf1 = '/etc/nginx/sites-available/%s.conf' % env.webuser

    src = 'conf/nginx.{}conf.template'.format('secure.' if secure else '')

    upload_template(
            src, nginx_conf1,
            {
                'host': env.vhost,
                'redirect_host': env.redirect_host,
                'dir': env.code_dir,
                'port': env.gunicorn_port,
            },
            use_sudo=True,
            use_jinja=True,
    )

    run('sudo rm -f /etc/nginx/sites-enabled/default')

    nginx_conf2 = '/etc/nginx/sites-enabled/%s.conf' % env.webuser
    run('sudo ln -fs %s %s' % (nginx_conf1, nginx_conf2))

    run('sudo nginx -t')
    run('sudo service nginx start')
    run('sudo service nginx reload')


@task
def celery_setup():
    with cd(env.code_dir):
        upload_template('conf/worker.sh.template',
                        env.code_dir + 'worker.sh',
                        {
                            'venv': env.venv_dir,
                        }, mode=0777, use_jinja=True)


@task
def gunicorn_setup():
    with cd(env.code_dir):
        upload_template('conf/server.sh.template',
                        env.code_dir + 'server.sh',
                        {
                            'venv': env.venv_dir,
                            'port': env.gunicorn_port,
                            'pidfile': env.pidfile,
                        }, mode=0777, use_jinja=True)


@task
def supervisor_reread():
    run("sudo supervisorctl reread")
    run("sudo supervisorctl update")


@task
def supervisor_setup():
    with cd(env.code_dir):
        upload_template('conf/supervisor.conf.template',
                        env.code_dir + 'conf/supervisor.conf',
                        {
                            'dir': env.code_dir,
                            'webuser': env.webuser,
                            'logdir': env.log_dir,
                        }, mode=0777, use_jinja=True)

        run('sudo ln -fs %sconf/supervisor.conf /etc/supervisor/conf.d/%s.conf'
            % (env.code_dir, env.webuser))
    supervisor_reread()
    # run("sudo supervisorctl start %s" % env.webuser)


@task
def project_mkdirs():
    """Creates empty directories for logs, uploads and search indexes"""
    with cd(env.code_dir):
        run('mkdir -pv conf')
        run('mkdir -pv %s' % env.log_dir)

        dirs = 'uploads'
        run('mkdir -pv {}'.format(dirs))
        run('sudo chown -v {} {}'.format(env.webuser, dirs))


@task
def status():
    run("sudo supervisorctl status")


@task
def setup_swap_file():
    sudo("dd if=/dev/zero of=/swapfile bs=1024 count=524288")
    sudo("chmod 600 /swapfile")
    sudo("mkswap /swapfile")
    sudo("swapon /swapfile")

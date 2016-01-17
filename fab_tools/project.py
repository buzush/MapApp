from contextlib import contextmanager
from random import choice

from fabric.api import *
from fabric.contrib.files import upload_template


def get_secret_key():
    return ''.join(
            [choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i
             in
             range(50)])


@contextmanager
def virtualenv(path):
    with cd(path):
        with prefix(env.venv_command):
            yield


@task
def upgrade_pip():
    with virtualenv(env.code_dir):
        run("pip install --upgrade pip", pty=False)


@task
def git_log():
    with virtualenv(env.code_dir):
        run("git log -n 1")


@task
def freeze():
    with virtualenv(env.code_dir):
        run("pip freeze")


@task
def reload_app():
    run("sudo kill -HUP `cat %s`" % env.pidfile)


@task
def deploy(restart=True, quick=False):
    # if restart:
    #     sudo("supervisorctl stop webmapapp_celery")
    with virtualenv(env.code_dir):
        run("git pull", pty=False)
        if not quick:
            run("pip install -r requirements.txt", pty=False)
            run("python manage.py migrate --noinput")
            # run("python manage.py createcachetable --database=cache")
            run("python manage.py update_permissions")
        run("python manage.py collectstatic --noinput")
        run("git log -n 1 --format=\"%ai %h\" > collected-static/version.txt")
        run("git log -n 1 > collected-static/version-full.txt")
    if restart:
        reload_app()
        # sudo("supervisorctl start webmapapp_celery")


@task
def quickdeploy():
    deploy(True, True)


@task
def clone_project():
    run("git clone %s %s" % (env.clone_url, env.code_dir), pty=False)


@task
def create_venv():
    run("virtualenv {} --prompt='({}) ' -p python3".format(env.venv_dir,
                                                           env.user))


@task
def create_local_settings():
    with cd(env.code_dir):
        upload_template('conf/prod_settings_template.py',
                        env.code_dir + 'mapapp/local_settings.py',
                        {
                            'webuser': env.webuser,
                            'host': env.vhost,
                            'secret_key': get_secret_key()
                        },
                        use_jinja=True)


@task
def reindex(rebuild=False):
    """Updates/rebuilds haystack search indexes for project"""
    cmd = "rebuild_index --noinput" if rebuild else "update_index"
    with virtualenv(env.code_dir):
        run("python manage.py {}".format(cmd))


@task
def createsuperuser():
    with virtualenv(env.code_dir):
        run("python manage.py createsuperuser")


@task
def del_pyc():
    with cd(env.code_dir):
        run("find . -name '*.pyc' -delete")


@task
def m(params):
    with virtualenv(env.code_dir):
        run("python manage.py {}".format(params))

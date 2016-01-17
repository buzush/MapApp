from fabric.api import *

from fab_tools.server import *
from fab_tools.project import *
from fab_tools import db
assert db
from fab_tools import dev
assert dev
import os.path

PROJ_DIR = os.path.abspath(os.path.dirname(__file__))
CONF_DIR = os.path.abspath(os.path.join(PROJ_DIR, 'conf'))

env.project = "mapapp"
env.user = "mapapp"
env.gunicorn_port = 9099
# env.clone_url = "git@github.com:hackita02/MapApp.git"
env.clone_url = "https://github.com/hackita02/MapApp.git"
env.webuser = "webmapapp"
env.code_dir = '/home/%s/MapApp/' % env.user
env.log_dir = '%slogs/' % env.code_dir
env.venv_dir = '/home/%s/.virtualenvs/mapapp' % env.user
env.venv_command = '.  %s/bin/activate' % env.venv_dir
env.pidfile = '/home/%s/mapapp.pid' % env.webuser
env.backup_dir = '/home/%s/backups' % env.user
env.instance = 'prod'
env.vhost = 'map.10x.org.il'
env.hosts = [env.vhost]
env.redirect_host = 'www.%s' % env.vhost



@task
def initial_project_setup():
    create_webuser_and_db()
    clone_project()
    create_venv()
    project_setup()


@task
def project_setup():
    project_mkdirs()
    create_local_settings()
    deploy(restart=False)
    celery_setup()
    gunicorn_setup()
    supervisor_setup()
    nginx_setup()

try:
    from local_fabfile import *
except ImportError:
    pass
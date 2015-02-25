from fabric.api import run, env, task, cd, sudo
from fabric.operations import get

"""
pip install fabric

how to run:
fab deploy -H root@demo.jedutils.com
"""


ENV_NAME = 'dental'
PORT = 8006


def gen_unicorn_cmd():
    return 'gunicorn -w 2 -b 127.0.0.1:{} -n {} dental.wsgi:application'.format(PORT, ENV_NAME)

@task
def deploy():
    prob_home = '/var/www/django/dental'
    with cd(prob_home):
        sudo('git pull')
        run('workon {} && python manage.py collectstatic --noinput'.format(ENV_NAME))
        run('workon {} && python manage.py migrate'.format(ENV_NAME))
        run('workon {} && {} &'.format(ENV_NAME, gen_unicorn_cmd()))

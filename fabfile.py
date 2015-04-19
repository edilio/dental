from fabric.api import run, env, task, cd, sudo
from fabric.operations import get

"""
pip install fabric

how to run:
fab deploy -i ~/.ssh/egallardojedutils.pem -H root@dental.jedutils.com
fab deploy -i ~/.ssh/egallardojedutils.pem -H ubuntu@52.16.31.196

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
        # run('workon {} && python manage.py collectstatic --noinput'.format(ENV_NAME))
        # run('workon {} && python manage.py migrate'.format(ENV_NAME))
        run('workon {} && {} &'.format(ENV_NAME, gen_unicorn_cmd()))

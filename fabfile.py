from fabric.api import run, env, task, cd, sudo
from fabric.operations import get
import time

"""
pip install fabric

how to run:
fab deploy -i ~/.ssh/egallardojedutils.pem -H ubuntu@dental.jedutils.com
fab deploy -i ~/.ssh/egallardojedutils.pem -H ubuntu@52.16.31.196

"""


ENV_NAME = 'dental'
PORT = 8006


def gen_unicorn_cmd(python_path=""):
    return '{}gunicorn -w 2 -b 127.0.0.1:{} -n {} dental.wsgi:application &'.format(python_path, PORT, ENV_NAME)

@task
def deploy():
    home = '/var/www/django/dental'
    python_path = "/home/ubuntu/.virtualenvs/{}/bin/".format(ENV_NAME)
    work_on_python = python_path + 'python'

    with cd(home):
        sudo('git pull')
        run('{} manage.py collectstatic --noinput'.format(work_on_python))
        run(' {} manage.py migrate'.format(work_on_python))

        ps = run('ps -ef | grep {} | head -n2'.format(ENV_NAME))
        sleep = False
        for line in ps.splitlines():
            if line.find('wsgi:application') > -1:
                i = line.find(' ')
                line = line[i:].strip()
                lst = line.split(' ')
                print lst[:10]
                run('kill -9 {}'.format(lst[0]))
                sleep = True
        if sleep:
            time.sleep(60)

        run(gen_unicorn_cmd(python_path))

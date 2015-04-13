#!/usr/bin/env python
ENV_NAME = 'dental'
PORT = 8006


def gen_unicorn_cmd():
    return 'gunicorn -w 2 -b 127.0.0.1:{} -n {} dental.wsgi:application'.format(PORT, ENV_NAME)


print gen_unicorn_cmd()

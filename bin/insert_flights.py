#!/usr/bin/env python
import os
import sys

#
APP_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(APP_DIR)
sys.path.append(os.path.dirname(APP_DIR))
print sys.path
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dental.settings')

import django
django.setup()

from marketing.models import Flight
from datetime import datetime

flights = """
2014-12-29, 2015-01-31
2015-01-02, 2015-02-28
2015-03-02, 2015-03-28
2015-03-30, 2015-04-25
2015-04-27, 2015-05-23
2015-05-25, 2015-06-27
2015-06-29, 2015-07-25
2015-07-27, 2015-08-29
2015-08-31, 2015-09-26
2015-09-28, 2015-10-24
2015-10-26, 2015-11-28
2015-11-30, 2015-12-26
"""


def get_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


for interval in flights.splitlines():
    interval = interval.strip()
    if interval:
        lst = interval.split(', ')
        print "processing:", get_date(lst[0]), get_date(lst[1])
        fs = Flight.objects.filter(first_day=get_date(lst[0]), last_day=get_date(lst[1]))
        if not fs.exists():
            Flight.objects.create(first_day=get_date(lst[0]), last_day=get_date(lst[1]))
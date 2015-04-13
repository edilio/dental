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

from fern.models import *

def save_to_sql(model):
    lst = model.objects.all()
    print "converting %s len: %d" %(model._meta.db_table, len(lst))
    for obj in lst:
        print obj.__unicode__()
        obj.save(using='mysql')


def save_all():
    models = [Source, Patient]
    for model in models:
        save_to_sql(model)



save_all()


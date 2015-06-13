#!/usr/bin/env python
import os
import sys
import csv
import codecs

from datetime import datetime

APP_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(APP_DIR)
sys.path.append(os.path.dirname(APP_DIR))
print sys.path
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dental.settings')

import django
django.setup()

from fern.models import HappyBirthdayPatient

# filename of the fiel to be imported
# it should have name, birthday, address
filename = 'hbpatients.csv'


def get_datetime(s):
    date_formats = ['%m/%d/%Y', '%m/%d/%y', '%m/%d/%Y %H:%M', '%m/%d/%Y %I:%M:%S %p', '%d-%b-%y  %H:%M:%S']
    for df in date_formats:
        try:
            d = datetime.strptime(s, df)
            return d
        except:
            pass
    raise Exception(s + " is an invalid date time format")


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'ISO-8859-1') for cell in row]


def import_hb_patients():
    reader = unicode_csv_reader(open(filename))
    header = True
    for name, birth_date, address in reader:
        if header or (name == ''):
            header = False
            continue
        HappyBirthdayPatient.objects.create(fullname=name, birth_date=get_datetime(birth_date), address=address)

if __name__ == '__main__':
    import_hb_patients()
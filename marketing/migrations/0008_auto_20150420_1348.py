# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def insert_ad_types(apps, schema_editor):
    objects = apps.get_model("marketing", "AdType").objects
    objects.create(name='Radio')
    objects.create(name='TV')
    objects.create(name='Flyer')


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_adtype'),
    ]

    operations = [
        migrations.RunPython(insert_ad_types),
    ]

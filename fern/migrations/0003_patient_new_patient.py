# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fern', '0002_auto_20150222_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='new_patient',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

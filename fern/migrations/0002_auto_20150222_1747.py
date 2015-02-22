# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fern', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='tour_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'F', b'Female'), (b'M', b'Male')]),
            preserve_default=True,
        ),
    ]

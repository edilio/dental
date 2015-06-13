# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fern', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HappyBirthdayPatient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=120)),
            ],
        ),
    ]

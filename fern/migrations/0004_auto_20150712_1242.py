# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fern', '0003_happybirthdaypatient_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happybirthdaypatient',
            name='treatment',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, b'Implants'), (1, b'Crowns'), (2, b'Laser'), (3, b'Surgery from July-2015')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_auto_20150419_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='office',
            field=models.ForeignKey(blank=True, to='marketing.DentalOffice', null=True),
        ),
    ]

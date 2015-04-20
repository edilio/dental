# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0009_vehicle_ad_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='flight',
            field=models.ForeignKey(default=True, blank=True, to='marketing.Flight'),
        ),
    ]

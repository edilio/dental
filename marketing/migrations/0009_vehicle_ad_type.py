# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0008_auto_20150420_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='ad_type',
            field=models.ForeignKey(default=1, to='marketing.AdType'),
        ),
    ]

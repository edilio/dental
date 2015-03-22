# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import marketing.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='year',
            field=models.PositiveSmallIntegerField(default=marketing.models.guess_year),
        ),
    ]

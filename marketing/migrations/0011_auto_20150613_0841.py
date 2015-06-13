# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0010_lead_flight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='entered_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import marketing.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_lead_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='DentalOffice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='flight',
            name='number',
            field=models.PositiveIntegerField(default=marketing.models.next_flight),
        ),
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='lm',
            field=models.BooleanField(default=False, help_text=b'Left Message'),
        ),
    ]

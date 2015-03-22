# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketing', '0002_auto_20150321_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('comments', models.TextField(null=True, blank=True)),
                ('lm', models.BooleanField(default=True, help_text=b'Left Message')),
                ('appointment_date', models.DateTimeField(null=True, blank=True)),
                ('entered_date', models.DateField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(to='marketing.Category')),
                ('entered_by', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(to='marketing.Vehicle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpotTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scheduled', models.DateTimeField(null=True, blank=True)),
                ('air_time', models.DateTimeField(null=True, blank=True)),
                ('vehicle', models.ForeignKey(to='marketing.Vehicle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

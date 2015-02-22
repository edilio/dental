# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True, choices=[(b'F', b'Feminine'), (b'M', b'Masculine')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patient',
            name='source',
            field=models.ForeignKey(to='fern.Source'),
            preserve_default=True,
        ),
    ]

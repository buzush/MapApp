# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(verbose_name='location', srid=4326)),
                ('radius', models.PositiveSmallIntegerField(default=200, verbose_name='radius')),
            ],
        ),
    ]

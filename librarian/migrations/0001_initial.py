# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content_type', models.CharField(max_length=3, choices=[('IMG', 'תמונה'), ('SNG', 'שיר'), ('MAP', 'מפה'), ('TRV', 'יומן מסע'), ('VID', 'קטע וידאו'), ('OTR', 'אחר')], verbose_name='סוג התוכן')),
                ('name', models.CharField(max_length=20, verbose_name='שם או כותרת')),
                ('description', models.CharField(max_length=200, verbose_name='תיאור התוכן')),
                ('link', models.URLField(verbose_name='קישור לתוכן')),
                ('date', models.DateField(verbose_name='תאריך התוכן')),
            ],
            options={
                'verbose_name_plural': 'תכנים',
                'verbose_name': 'content',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('additional_text', models.CharField(max_length=30, verbose_name='additional text')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='location')),
                ('radius', models.PositiveSmallIntegerField(default=200, verbose_name='radius')),
            ],
            options={
                'verbose_name_plural': 'sites',
                'verbose_name': 'site',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='site',
            field=models.ForeignKey(to='librarian.Site', verbose_name='אתר מקושר'),
        ),
    ]

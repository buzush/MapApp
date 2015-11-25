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
                ('content_id', models.AutoField(serialize=False, primary_key=True)),
                ('content_type', models.CharField(max_length=3, choices=[('IMG', 'תמונה'), ('SNG', 'שיר'), ('MAP', 'מפה'), ('TRV', 'יומן מסע'), ('VID', 'קטע וידאו'), ('OTR', 'אחר')], verbose_name='סוג התוכן')),
                ('name', models.CharField(max_length=20, verbose_name='שם או כותרת')),
                ('description', models.CharField(max_length=200, verbose_name='תיאור התוכן')),
                ('link', models.URLField(verbose_name='קישור לתוכן')),
                ('date', models.DateField(verbose_name='תאריך התוכן')),
            ],
            options={
                'verbose_name_plural': 'תכנים',
                'verbose_name': 'תוכן',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.AutoField(serialize=False, primary_key=True, verbose_name='מספר אתר')),
                ('site_name', models.CharField(max_length=30, verbose_name='שם אתר')),
                ('additional_text', models.CharField(max_length=30, verbose_name='טקסט נוסף')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
                ('radius', models.PositiveSmallIntegerField(default='200', verbose_name='רדיוס')),
            ],
            options={
                'verbose_name_plural': 'אתרים',
                'verbose_name': 'אתר',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='site',
            field=models.ForeignKey(to='librarian.Site', verbose_name='אתר מקושר'),
        ),
    ]

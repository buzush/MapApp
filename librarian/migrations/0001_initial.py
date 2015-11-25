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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('IMG', 'תמונה'), ('SNG', 'שיר'), ('MAP', 'מפה'), ('TRV', 'יומן מסע'), ('VID', 'קטע וידאו'), ('OTR', 'אחר')], max_length=3, verbose_name='סוג התוכן')),
                ('name', models.CharField(verbose_name='שם או כותרת', max_length=20)),
                ('description', models.CharField(verbose_name='תיאור התוכן', max_length=200)),
                ('link', models.URLField(verbose_name='קישור לתוכן')),
                ('date', models.DateField(verbose_name='תאריך התוכן')),
            ],
            options={
                'verbose_name': 'תוכן',
                'verbose_name_plural': 'תכנים',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='שם אתר', max_length=30)),
                ('additional_text', models.CharField(verbose_name='טקסט נוסף', max_length=30)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=(3736198.0, 3922079.0), srid=4326)),
                ('radius', models.PositiveSmallIntegerField(default=200, verbose_name='רדיוס')),
            ],
            options={
                'verbose_name': 'אתר',
                'verbose_name_plural': 'אתרים',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='site',
            field=models.ForeignKey(verbose_name='אתר מקושר', to='librarian.Site'),
        ),
    ]

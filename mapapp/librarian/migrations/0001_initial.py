# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('link', models.URLField(verbose_name='קישור לתוכן')),
                ('date', models.DateField(verbose_name='תאריך התוכן')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.AutoField(primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=30)),
                ('additional_text', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=10)),
                ('radius', models.PositiveSmallIntegerField(default='200')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='site',
            field=models.ForeignKey(to='librarian.Site'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_auto_20160116_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='creator',
            field=models.CharField(null=True, max_length=14, verbose_name='יוצר/ת'),
        ),
        migrations.AlterField(
            model_name='content',
            name='creator_2',
            field=models.CharField(null=True, max_length=14, verbose_name='יוצר/ת נוספ/ת'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date',
            field=models.DateField(null=True, verbose_name='תאריך התוכן'),
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.CharField(null=True, max_length=200, verbose_name='תיאור התוכן'),
        ),
        migrations.AlterField(
            model_name='content',
            name='performing',
            field=models.CharField(null=True, max_length=14, verbose_name='מבצע/ת'),
        ),
    ]

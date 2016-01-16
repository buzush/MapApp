# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_auto_20160116_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='creator',
            field=models.CharField(max_length=14, verbose_name='יוצר/ת', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='creator_2',
            field=models.CharField(max_length=14, verbose_name='יוצר/ת נוספ/ת', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='date',
            field=models.DateField(verbose_name='תאריך התוכן', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.CharField(max_length=200, verbose_name='תיאור התוכן', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='performing',
            field=models.CharField(max_length=14, verbose_name='מבצע/ת', null=True, blank=True),
        ),
    ]

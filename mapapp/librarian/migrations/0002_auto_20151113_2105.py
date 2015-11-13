# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name_plural': 'תכנים', 'verbose_name': 'תוכן'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'verbose_name_plural': 'אתרים', 'verbose_name': 'אתר'},
        ),
        migrations.AddField(
            model_name='content',
            name='content_type',
            field=models.CharField(choices=[('IMG', 'תמונה'), ('SNG', 'שיר'), ('MAP', 'מפה'), ('TRV', 'יומן מסע'), ('VID', 'קטע וידאו'), ('OTR', 'אחר')], default='SNG', verbose_name='סוג התוכן', max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.CharField(verbose_name='תיאור התוכן', max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(verbose_name='שם או כותרת', max_length=20),
        ),
        migrations.AlterField(
            model_name='content',
            name='site',
            field=models.ForeignKey(verbose_name='אתר מקושר', to='librarian.Site'),
        ),
        migrations.AlterField(
            model_name='site',
            name='additional_text',
            field=models.CharField(verbose_name='טקסט נוסף', max_length=30),
        ),
        migrations.AlterField(
            model_name='site',
            name='location',
            field=models.CharField(verbose_name='מיקום', max_length=10),
        ),
        migrations.AlterField(
            model_name='site',
            name='radius',
            field=models.PositiveSmallIntegerField(default='200', verbose_name='רדיוס'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_id',
            field=models.AutoField(verbose_name='מספר אתר', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_name',
            field=models.CharField(verbose_name='שם אתר', max_length=30),
        ),
    ]

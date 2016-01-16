# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content_collection',
            field=models.CharField(max_length=10, verbose_name='אוסף', default='BaiTmuna', choices=[('BaiTmuna', 'ביתמונה'), ('WahrmanAlbum', 'אוסף עקב ורמן'), ('Aleksandrowicz', 'מאגר תצלומי זאב אלכסנדרוביץ'), ('Tsalmania', 'הצלמניה'), ('Schwadron', 'אוסף הפורטרים של אברהם שבדרון'), ('Lenkin', 'מאגר לנקין'), ('Ephemera', 'מסע בזמן'), ('Music', 'ארכיון המוסיקה'), ('Maps', 'אוסף המפות')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='creator',
            field=models.CharField(max_length=14, verbose_name='יוצר/ת', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='creator_2',
            field=models.CharField(max_length=14, verbose_name='יוצר/ת נוספ/ת', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='performing',
            field=models.CharField(max_length=14, verbose_name='מבצע/ת', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='site',
            field=models.ForeignKey(related_name='contents', verbose_name='אתר מקושר', to='librarian.Site'),
        ),
    ]

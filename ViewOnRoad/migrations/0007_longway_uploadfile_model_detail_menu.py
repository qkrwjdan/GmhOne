# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-24 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViewOnRoad', '0006_auto_20190223_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='longway_uploadfile_model',
            name='detail_menu',
            field=models.CharField(choices=[('ASIA', 'ASIA'), ('CHINA', 'CHINA'), ('TAI', 'TAI'), ('MIDDEL_EAST', 'MIDDEL_EAST'), ('EUROPE', 'EUROPE'), ('AFRICA', 'AFRICA'), ('AMERICA', 'AMERICA')], default='ASIA', max_length=10),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-24 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViewOnRoad', '0007_longway_uploadfile_model_detail_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyonroad_uploadfile_model',
            name='detail_menu',
            field=models.CharField(choices=[('MYROAD', '나의길이야기'), ('RESTAURANT', '맛집으로 가는길'), ('HISTORY', '역사 속으로 가는길'), ('FESTIVAL', '축제가는 길'), ('HARDROAD', '고행의 길'), ('ADVENTURE', '탐험의 길'), ('REST', '휴식의 길')], default='MYROAD', max_length=10),
        ),
        migrations.AlterField(
            model_name='longway_uploadfile_model',
            name='detail_menu',
            field=models.CharField(choices=[('ASIA', '아시아'), ('CHINA', '중국'), ('TAI', '태국'), ('MIDDEL_EAST', '중동'), ('EUROPE', '유럽'), ('AFRICA', '아프리카'), ('AMERICA', '아메리카')], default='ASIA', max_length=10),
        ),
    ]

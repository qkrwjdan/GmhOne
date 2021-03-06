# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-28 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViewOnRoad', '0008_auto_20190224_1355'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
        migrations.DeleteModel(
            name='UploadFile',
        ),
        migrations.AddField(
            model_name='longway_uploadfile_model',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roadview_uploadfile_model',
            name='detail_menu',
            field=models.CharField(choices=[('서울', '서울'), ('경기도', '경기도'), ('충청도', '충청도'), ('전라도', '전라도'), ('강원도', '강원도'), ('경상도', '경상도'), ('제주도', '제주도')], default='서울', max_length=5),
        ),
        migrations.AddField(
            model_name='roadview_uploadfile_model',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='storyonroad_uploadfile_model',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]

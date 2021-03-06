# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-18 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ViewOnRoad', '0004_auto_20190212_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='longWay_uploadFile_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='roadview_uploadFile_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='storyonroad_uploadFile_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='uploads/%y/%m/%d'),
        ),
    ]

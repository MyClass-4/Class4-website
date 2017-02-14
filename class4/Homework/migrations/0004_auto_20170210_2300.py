# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 15:00
from __future__ import unicode_literals

import Homework.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0003_auto_20170210_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework_item',
            options={'verbose_name': '\u5df2\u63d0\u4ea4\u4f5c\u4e1a', 'verbose_name_plural': '\u5df2\u63d0\u4ea4\u4f5c\u4e1a'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='\u8bfe\u7a0b\u540d\u79f0', max_length=200, verbose_name='\u8bfe\u7a0b\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='homework_item',
            name='homework_file',
            field=models.FileField(default='homework/default', upload_to=Homework.models.upload_homework, verbose_name='\u4f5c\u4e1a\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='homework_item',
            name='submit_time',
            field=models.DateField(auto_now=True, verbose_name='\u63d0\u4ea4\u65f6\u95f4'),
        ),
    ]
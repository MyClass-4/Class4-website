# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20170209_1530'),
        ('Homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='\u6807\u9898', max_length=250, verbose_name='\u6807\u9898')),
                ('submit_time', models.DateField(auto_now_add=True, verbose_name='\u63d0\u4ea4\u65f6\u95f4')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework_items_of_user_set', related_query_name='homeworkItemOfUser', to='User.User', verbose_name='\u4f5c\u8005')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework_item_of_homework_set', related_query_name='homeworkItemOfHomework', to='Homework.Homework', verbose_name='\u4f5c\u4e1a\u540d\u79f0')),
            ],
            options={
                'ordering': ['-submit_time'],
                'verbose_name': '\u5df2\u63d0\u4ea4\u4f5c\u4e1a',
                'verbose_name_plural': '\u5df2\u63d0\u4ea4\u4f5c\u4e1a',
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='\u8bfe\u7a0b', max_length=200, verbose_name='\u8bfe\u7a0b')),
                ('teacher', models.CharField(blank=True, default='\u8001\u5e08', max_length=200, verbose_name='\u8001\u5e08')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='\u4f5c\u4e1a', max_length=250, verbose_name='\u4f5c\u4e1a\u540d\u79f0')),
                ('detail', models.CharField(blank=True, default='\u5907\u6ce8', max_length=500, verbose_name='\u5907\u6ce8')),
                ('state', models.BooleanField(default=False, verbose_name='\u72b6\u6001')),
                ('release_time', models.DateField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('deadline_time', models.DateField(verbose_name='\u622a\u6b62\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework_of_course_set', related_query_name='postingOfCourse', to='Homework.Course', verbose_name='\u8bfe\u7a0b')),
            ],
            options={
                'ordering': ['-release_time'],
                'verbose_name': '\u4f5c\u4e1a',
                'verbose_name_plural': '\u4f5c\u4e1a',
            },
        ),
    ]

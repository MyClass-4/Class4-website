# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from User.models import User
from class4 import settings
import os

# Create your models here.


class Course(models.Model):
    name = models.CharField('课程名称', max_length=200, blank=False, null=False, default='课程名称')
    teacher = models.CharField('老师', max_length=200, blank=True, default='老师')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'


class Homework(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程', related_name='homework_of_course_set', \
                                related_query_name='homeworkOfCourse', null=False)
    name = models.CharField('作业名称', max_length=250, blank=False, default='作业')
    detail = models.CharField('备注', max_length=500, blank=True, default='备注')
    is_over = models.BooleanField('状态', default=False)
    release_time = models.DateField('发布时间', auto_now_add=True)
    deadline = models.DateField('截止时间', auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '作业'
        verbose_name_plural = '作业'
        ordering = ['-release_time']


def upload_homework(instance, filename):
    pre_file_dir = os.path.join(settings.MEDIA_ROOT, ('homework/%s/%s/%s' % (instance.homework.course.name, instance.homework.name,filename))).replace('\\', '/')
    if os.path.exists(pre_file_dir):
        os.remove(pre_file_dir)
    return 'homework/%s/%s/%s' % (instance.homework.course.name, instance.homework.name, filename)

class Homework_item(models.Model):
    homework = models.ForeignKey(Homework, verbose_name='作业名称', related_name='homework_item_of_homework_set', \
                                    related_query_name='homeworkItemOfHomework', null=False)
    homework_file = models.FileField(upload_to=upload_homework, verbose_name='作业文件', default='homework/default')
    title = models.CharField('标题', max_length=250, blank=False, default='标题')
    author = models.ForeignKey(User, verbose_name='作者', related_name='homework_items_of_user_set', \
                                related_query_name='homeworkItemOfUser', null=False)
    submit_time = models.DateField('提交时间', auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '已提交作业'
        verbose_name_plural = '已提交作业'

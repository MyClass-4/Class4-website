# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from User.models import User
# Create your models here.


class Topic(models.Model):
    author = models.ForeignKey(User, verbose_name='作者', related_name='topic_of_author_set', \
                               related_query_name='topicOfAuthor', null=False)
    title = models.CharField('标题', max_length=250, blank=False, null=False, default='标题')
    content = models.TextField('内容', default='')
    release_time = models.DateField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '话题'
        verbose_name_plural = '话题'
        ordering = ['-release_time']


class Posting(models.Model):
    author = models.ForeignKey(User, verbose_name='作者', related_name='posting_of_author_set', \
                               related_query_name='postingOfAuthor', null=False)
    topic = models.ForeignKey(Topic, verbose_name='主题', related_name='posting_of_topic_set', \
                              related_query_name='postingOfTopic', null=False)
    content = models.TextField('内容', default='')
    like = models.IntegerField('点赞', default=0)
    release_time = models.DateField('发布时间', auto_now_add=True)

    def __unicode__(self):
        # return self.id
        # 会导致 coercing to Unicode: need string or buffer, int found
        return "posting_{0}".format(self.id)

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'
        ordering = ['-release_time']


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='作者', related_name='comment_of_author_set', \
                               related_query_name='commentOfAuthor', null=False)
    posting = models.ForeignKey(Posting, verbose_name='帖子', related_name='comment_of_posting_set', \
                                related_query_name='commentOfPosting', null=False)
    content = models.TextField('内容', default='')
    like = models.IntegerField('点赞', default=0)
    release_time = models.DateField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return 'comment', self.id

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ['-release_time']



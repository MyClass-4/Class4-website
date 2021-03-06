# -*-coding: utf-8 -*-
from __future__ import unicode_literals

from class4 import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import hashlib
import os


def encry(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()
# Create your models here.

def upload_avatar(instance, filename):
    fn, ext = os.path.splitext(filename)
    fn = instance.user_name
    filename = fn + ext
    pre_file_dir = os.path.join(settings.MEDIA_ROOT, ('avatars/%s' % (filename))).replace('\\', '/')
    # 删除同名/之前的头像
    if os.path.exists(pre_file_dir):
        os.remove(pre_file_dir)
    return os.path.join('avatars', filename)


# @python_2_unicode_compatible
class User(models.Model):
    user_name = models.CharField('用户名', max_length=200, default='')
    real_name = models.CharField('真名', max_length=200, default='')
    password = models.CharField('密码', max_length=200, default=encry('123456'), blank=True)
    sign = models.CharField('个性签名', max_length=200, default='')
    avatar = models.ImageField(upload_to=upload_avatar, default='avatars/default.jpg')

    # def __ str__(self):
    #     return self.user_name

    def __unicode__(self):
        return self.user_name

    class Meta:
        # 单数元信息
        verbose_name = '用户'
        # 复数元信息
        verbose_name_plural = '用户'

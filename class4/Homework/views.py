# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from class4 import settings
from User.models import User
from Homework.models import Course, Homework, Homework_item
import datetime
import os
import json
# Create your views here.


def index(request):
    if request.session.get('user_name', None):
        homework_list = Homework.objects.all()
        course_list = Course.objects.all()
        info = {'homework_list': homework_list, 'course_list': course_list}
        return render(request, 'Homework/upload_homework_page.html', info)
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def upload_homework(request):
    if request.session.get('user_name', None):
        print '================>>>>>'
        user_name = request.session['user_name']
        files = request.FILES['homework_file']
        print '==>', files
        course_name = request.POST.get('course_name')
        homework_name = request.POST.get('homework_name')

        course = Course.objects.get(name=course_name)
        user = User.objects.get(user_name=user_name)
        homework = Homework.objects.get(course=course, name=homework_name)
        title = '%s_%s_%s' % (course_name, homework_name, user_name)
        homework_item, not_exist = Homework_item.objects.get_or_create(homework=homework, author=user, title=title)
        if not_exist:
            # 初次保存作业
            homework_item.homework_file = files
            homework_item.save()
            info = {}
            info['success'] = 1
            info['msg'] = ''
            print '==> create homeworkitem successfully'
            return JsonResponse(info)
        else:
            # 覆盖已有作业文件
            # 此处假设在前端已经正则检验过文件名，每个作业文件名都是相同的
            # pre_file_dir = os.path.join(settings.MEDIA_ROOT, ('homework/%s/%s/%s/%s' % (course_name, homework_name, user_name, files.name))).replace('\\', '/')
            # # 如果已存在该文件先删除
            # if os.path.exists(pre_file_dir):
            #     os.remove(pre_file_dir)

            homework_item.homework_file = files
            homework_item.save()
            info = {}
            info['success'] = 1
            info['msg'] = '覆盖文件成功'
            print '==> cover homeworkItem successfully'
            return JsonResponse(info)
            # return HttpResponseRedirect(reverse('homework_index'))
    else:
        return HttpResponseRedirect(reverse('login'))


def homework_info(request, homework_id):
    if request.session.get('user_name', None):
        homework = Homework.objects.get(id=homework_id)
        info = {'homework': homework}
        return render(request, 'Homework/homework_info.html', info)
    else:
        return HttpResponseRedirect(reverse('login'))

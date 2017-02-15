# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from class4 import settings
from User.models import User
from Forum.models import *
import datetime
import json
import os
# Create your views here.


def index(request):
    if request.session.get('user_name', None):
        topic_list = Topic.objects.all()
        info = {'topic_list': topic_list}
        return render(request, 'Forum/forum_index.html', info)
    else:
        return HttpResponseRedirect(reverse('login'))


def topic_info(request, topic_id):
    if request.session.get('user_name', None):
        topic = Topic.objects.get(id=topic_id)
        posting_list = topic.posting_of_topic_set.order_by('release_time')
        print '===>>',posting_list
        info = {'topic': topic, 'posting_list': posting_list}
        print info
        return render(request, 'Forum/topic_info.html', info)
    else:
        return HttpResponseRedirect(reverse('login'))


def create_topic(request):
    if request.session.get('user_name', None):
        if request.method == 'POST':
            user = User.objects.get(user_name=request.session['user_name'])
            title = request.POST.get('title', None)
            content = request.POST.get('content', None)
            topic = Topic.objects.create(author=user, title=title, content=content)
            topic.save()
            return HttpResponseRedirect(reverse('forum_index'))
        else:
            return render(request, 'Forum/create_topic.html')
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def uploadImg(request):
    if request.session.get('user_name', None) and request.method == 'POST':
        files = request.FILES['imgFile']
        today = datetime.datetime.today()
        file_dir = os.path.join(settings.MEDIA_ROOT, ('simditor/%d/%d/%d' % (today.year, today.month, today.day))).replace('\\', '/')
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_path = os.path.join(file_dir, files.name).replace('\\', '/')
        upload_url = os.path.join(settings.MEDIA_URL, ('simditor/%d/%d/%d'%(today.year, today.month, today.day)), files.name).replace('\\', '/')
        info = {}
        print '==>> upload img'
        print upload_url
        try:
            open(file_path, 'wb+').write(files.read())  # 上传文件
            info['error'] = 0
            info['url'] = upload_url
            print '===> success'
            return HttpResponse(json.dumps(info))
        except:
            info['error'] = False
            info['url'] = upload_url
            print '====> fail'
            return HttpResponse(json.dumps(info))
    else:
        return HttpResponseRedirect(reverse('login'))


def create_posting(request, topic_id):
    if request.session.get('user_name', None) and request.method == 'POST':
        user = User.objects.get(user_name=request.session['user_name'])
        content = request.POST.get('content', None)
        # try:
        topic = Topic.objects.get(id=topic_id)
        posting = Posting.objects.create(author=user, content=content, topic=topic)
        posting.save()
        print posting
        print posting.content
        return HttpResponseRedirect(reverse('forum_topic', kwargs={'topic_id': int(topic_id)}))
        # except:
        #     return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))


def create_comment(request, posting_id):
    if request.session.get('user_name', None) and request.method == 'POST':
         user = User.objects.get(user_name=request.session['user_name'])
         try:
             posting = Posting.objects.get(id=posting_id)
             comment_content = request.POST.get('myComment')
             comment = Comment.objects.create(author=user, posting=posting, content=comment_content)
             comment.save()
             return HttpResponseRedirect(reverse('forum_topic', kwargs={'topic_id': posting.topic.id}))
         except:
             return HttpResponse('error1')
             # return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponse('error2')
        return HttpResponseRedirect(reverse('login'))
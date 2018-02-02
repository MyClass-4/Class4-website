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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def getHotTopics(Topic):
    hot_topic_list = list(Topic.objects.order_by('postingOfTopic').distinct())
    hot_topic_list = hot_topic_list[0:5]
    return  hot_topic_list

def getSomePage(paginator, current_num):
    num_list = list(paginator.page_range)
    if current_num - 4 < 0:
        if current_num + 4 < num_list[-1]:
            return num_list[0:6]
        else:
            return num_list[0:]
    else:
        if current_num + 3 <= num_list[-1]:
            return num_list[current_num - 3:current_num + 3]
        else:
            return num_list[num_list[-1] - 6:]

def index(request):
    if request.session.get('user_name', None):
        if request.method == 'POST':
            key_word = request.POST.get('key_word', '')
            option = request.POST.get('option', 'title')
            key_word_list = key_word.split(' ')
            q = Q()
            if option == 'title':
                for key in key_word_list:
                    q.add(Q(title__icontains=key), Q.OR)
            elif(option == 'author'):
                for key in key_word_list:
                    q.add(Q(author__real_name=key), Q.OR)
            elif(option == 'content'):
                for key in key_word_list:
                    q.add(Q(content__icontains=key), Q.OR)
            else:
                for key in key_word_list:
                    q.add(Q(title__icontains=key), Q.OR)
            topic_list = Topic.objects.filter(q)
        else:
            topic_list = Topic.objects.all()

        hot_topic_list = getHotTopics(Topic)
        # 分页
        paginator = Paginator(topic_list, 6);
        page_num = request.GET.get('page', 1)
        try:
            current_page = paginator.page(page_num)
        except PageNotAnInteger:
            current_page = paginator.page(1)
        except EmptyPage:
            current_page = paginator.page(paginator.num_pages)

        topic_list = current_page.object_list.all()
        num_list = getSomePage(paginator, current_page.number)
        info = {'topic_list': topic_list, 'num_list': num_list, 'current_page':current_page, 'last_page_num':paginator.num_pages, 'hot_topic_list':hot_topic_list}
        return render(request, 'Forum/forum_index.html', info)
    else:
        return HttpResponseRedirect(reverse('login'))



def topic_info(request, topic_id):
    if request.session.get('user_name', None):
        topic = Topic.objects.get(id=topic_id)
        posting_list = topic.posting_of_topic_set.order_by('release_time')
        hot_topic_list = getHotTopics(Topic)
        # 分页
        paginator = Paginator(posting_list, 6)
        page_num = request.GET.get('page', 1)
        try:
            current_page = paginator.page(page_num)
        except PageNotAnInteger:
            current_page = paginator.page(1)
        except EmptyPage:
            current_page = paginator.page(paginator.num_pages)

        user = User.objects.get(user_name=request.session['user_name'])
        posting_list = current_page.object_list.all()
        # 获取相邻页码
        num_list = getSomePage(paginator, current_page.number)
        info = {'topic': topic, 'posting_list': posting_list, 'current_page': current_page, 'num_list': num_list, 'hot_topic_list': hot_topic_list, 'user': user}
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
        try:
            topic = Topic.objects.get(id=topic_id)
            posting = Posting.objects.create(author=user, content=content, topic=topic)
            posting.save()
            print posting
            print posting.content
            return HttpResponseRedirect(reverse('forum_topic', kwargs={'topic_id': int(topic_id)}))
        except:
            return HttpResponseRedirect(reverse('index'))
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
             return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('login'))

def create_posting_like(request, posting_id):
    if request.session.get('user_name', None) and request.method == 'POST':
         user = User.objects.get(user_name=request.session['user_name'])
         try:
             posting = Posting.objects.get(id=posting_id)
             if posting.like.filter(id=user.id).count() == 0:
                 posting.like.add(user)
                 posting.save()
             return HttpResponseRedirect(reverse('forum_topic', kwargs={'topic_id': posting.topic.id}))
         except:
             return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))

def create_comment_like(request, comment_id):
    if request.session.get('user_name', None) and request.method == 'POST':
        user = User.objects.get(user_name=request.session['user_name'])
        try:
            posting = Comments.objects.get(id=comment_id)
            if comment.like.filter(id=user.id).count() == 0:
                comment.like.add(user)
                comment.save()
            return HttpResponseRedirect(reverse('forum_topic', kwargs={'topic_id': posting.topic.id}))
        except:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))

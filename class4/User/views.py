# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

import hashlib
from User.models import User
# Create your views here.

def encry(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()

def login(request):
    if request.method == 'POST':
        # 教程上有个get_object_or_404的用法，这里应该也可以用
        user_name = request.POST.get('user_name', None)
        password = request.POST.get('password', None)
        password = encry(password)

        try:
            user = User.objects.get(user_name = user_name, password = password)
            request.session['user_name'] = user_name
            # ?? reverse redirect
            return HttpResponseRedirect(reverse('index'))
        except:
            # 这里修改成返回JSON信息 ********************************************
            return HttpResponse('login error')
    else:
        return render(request, 'User/login.html')

def logout(request):
    if request.session.get('user_name', None):
        del request.session['user_name']
    return HttpResponseRedirect(reverse('login'))

def index(request):
    if request.session.get('user_name', None):# 登录过的
        user = User.objects.get(user_name = request.session['user_name'])
        # todo: add message
        info = {'user': user}
        return render(request, 'User/index.html', info)
    else:
        return HttpResponseRedirect(reverse('login'))

# 鉴于我们自己可以在djanog admin里面创立所有认证账户，所以将 注册 功能删去

# def register(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         password = request.POST.get('password')
#         password_twice = request.POST.get('password_twice')
#
#         if password != password_twice:
#             return HttpResponse("两次输入的密码不一致")
#         password = encry(password)
#         # 如果在user中找到了，即已经注册过的，not exist赋值true
#         user, not_exist = User.objects.get_or_create(user_name = user_name, password = password)
#         if not_exist:
#             user.save()
#             return HttpResponseRedirect(reverse('login'))
#         else:
#             return HttpResponse("error: 该用户已存在")
#     else:
#         return render(request, 'User/register.html')

# change profile
def profile(request):
    if request.method == 'POST':
        # 不允许用户修改用户名，因为用户名就是unique tag
        password = request.POST.get('password')
        password_twice = request.POST.get('password_twice')
        if password != password_twice:
            return HttpResponse("两次输入的密码不一致")
        password = encry(password)
        user = User.objects.get(user_name = request.session['user_name'])
        user.password = password
        user.sign = request.POST.get('sign')
        user.avatar = request.FILES.get('avatar')
        user.save()
        return HttpResponse("修改成功")
    else:
        user = User.objects.get(user_name = request.session['user_name'])
        return render(request, 'User/profile.html', { 'user': user })

def changeAvatar(request):
    if request.method == 'POST':
        user = User.objects.get(user_name = request.session['user_name'])
        user.avatar = request.FILES.get('avatar')
        user.save()
        return HttpResponse("修改成功")
    else:
        return render(request, 'User/changeavatar.html')

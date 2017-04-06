# -*- coding -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
import urllib2
import urllib
import urlparse
import lxml.html
import os

# Create your views here.



def download(url, user_agent='wswp', proxy=None, error_num=5):
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    # can also add headers in opener
    # opener.addheaders({'User-agent': user_agent})
    if proxy:
        # proxy_params is a dict {url's scheme: url or proxy}
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
        print 'download success:', url
    except urllib2.URLError as e:
        print 'download error: ', e.reason
        html = None
        if error_num > 0 and hasattr(e, 'code') and e.code in range(500, 600):
            return download(url, user_agent, proxy, error_num - 1)
    return html



def index(request):
    info = {}
    if request.method == 'POST':
        url_seed = 'http://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=809002.661476&q='
        search = request.POST.get('search_item', None)
        search = urllib.quote(search)
        url = url_seed + search
        data = download(url)
        import pprint
        pprint.pprint(data)
        return JsonResponse({'aa':'a'})
    return render(request, 'WebScraping/index.html', info)


def search(request):
    if request.method == 'POST':
        # url_seed = 'http://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=75857.485279&q='
        # search = request.POST.get('search_item', None)
        # search = urllib.quote(search)
        # url = url_seed + search
        # print url
        # data = download(url)
        # print data.encode('utf-8')
        return JsonResponse({'da':'ss'})
    return HttpResponseRedirect(reverse('index'))

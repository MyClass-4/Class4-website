"""class4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from User.views import index as User_views_index
from django.conf.urls.static import static
from django.conf import settings
import django

urlpatterns = [
    url(r'^$', User_views_index, name='index'),
    url(r'^User/', include('User.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'Forum/', include('Forum.urls')),
    url(r'^Homework/', include('Homework.urls')),
]

urlpatterns += url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),

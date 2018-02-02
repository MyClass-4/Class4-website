from django.conf.urls import include, url
from . import views as User_views

urlpatterns = [
    url(r'^$', User_views.index, name='index'),
    url(r'^login$', User_views.login, name = 'login'),
    url(r'^logout$', User_views.logout, name = 'logout'),
]

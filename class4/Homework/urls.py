from django.conf.urls import include, url
from Homework import views as Homework_views

urlpatterns = [
    url(r'^$', Homework_views.index, name='homework_index'),
    url(r'^upload_homework$', Homework_views.upload_homework, name='upload_homework'),
    url(r'^homework/(?P<homework_id>\d+)$', Homework_views.homework_info, name='homework_info'),
]

from django.conf.urls import include, url
from Forum import views as Forum_view

urlpatterns = [
    url(r'^$', Forum_view.index, name='forum_index'),
    url(r'^topic/(?P<topic_id>\d+)$', Forum_view.topic_info, name='forum_topic'),
    url(r'^new$', Forum_view.create_topic, name='forum_create_topic'),
    url(r'^new_posting/(?P<topic_id>\d+)$', Forum_view.create_posting, name='forum_create_posting'),
    url(r'^uploadImg$', Forum_view.uploadImg, name='forum_uploadImg'),
]

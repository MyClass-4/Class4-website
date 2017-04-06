from django.conf.urls import include, url
from WebScraping import views as WebScraping_view

urlpatterns = [
   url(r'^$', WebScraping_view.index, name='webscraping_index'),
   url(r'^search$', WebScraping_view.search, name='webscraping_search'),
]

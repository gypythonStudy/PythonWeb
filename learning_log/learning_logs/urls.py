from django.conf.urls import url

from  . import  views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'indexMe', views.indexMe, name='indexMe'),
    url(r'info', views.info, name='info'),
    url(r'about', views.about, name='about'),
    url(r'gbook', views.gbook, name='gbook'),
    url(r'life', views.life, name='life'),
    url(r'list', views.list, name='list'),
    url(r'share', views.share, name='share'),
    url(r'time', views.time, name='time'),
]
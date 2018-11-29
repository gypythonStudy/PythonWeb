from django.conf.urls import url

from  . import  views
from learning_logs.views import IndexView, BlogDetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(),name='index'),
    # url(r'^$', views.index, name='index'),

    url(r'^topics/$', views.topics, name='topics'),
    url(r'indexMe', views.indexMe, name='indexMe'),
    url(r'info', views.info, name='info'),
    url(r'about', views.about, name='about'),
    url(r'gbook', views.gbook, name='gbook'),
    url(r'life', views.life, name='life'),
    url(r'list', views.list, name='list'),
    url(r'share', views.share, name='share'),
    url(r'time', views.time, name='time'),
    url(r'blog/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='blog_id'),
    # url(r'^blog/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='blog_id'),
]

# 配置全局404页面
hander404 = 'myblog.views.page_not_found'

# 配置全局505页面
hander505 = 'myblog.views.page_errors'
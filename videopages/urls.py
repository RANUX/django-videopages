# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from videopages.views.create import create_page
from videopages.views.edit import EditVideoView
from videopages.views.list import VideoPageListView
from views.page import VideoPageView

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


urlpatterns = patterns('',
    url(r'^$', VideoPageListView.as_view(), name='videopages_list'),
    url(r'^create/$', login_required(create_page), name='videopages_create'),
    url(r'^edit/(?P<slug>[\w-]+)/$', login_required(EditVideoView.as_view()), name='videopages_edit'),
    url(r'^(?P<url>.*)$', VideoPageView.as_view(), name='videopages_page'),
)
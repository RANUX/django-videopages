# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from videopages.views.edit import EditVideoView
from videopages.views.list import VideoPageListView, UserVideoPageListView
from views.page import VideoPageView

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


urlpatterns = patterns('',
    url(r'^$', VideoPageListView.as_view(), name='videopages_list'),
    url(r'^(?P<username>[\w]+)/edit/(?P<slug>[\w-]+)/$',
        permission_required('djangovideos.add_video')(
            permission_required('videopages.add_videopage')(login_required(EditVideoView.as_view()))
        ),
        name='videopages_edit'),
    url(r'^(?P<username>[\w]+)/create/$',
        permission_required('djangovideos.add_video')(
            permission_required('videopages.add_videopage')(login_required(EditVideoView.as_view()))
        ),
        name='videopages_create'),
    url(r'^(?P<username>[\w]+)/video/(?P<url>.*)$', VideoPageView.as_view(), name='videopages_page'),
    url(r'^(?P<username>[\w]+)/(?P<url>.*)/$', VideoPageView.as_view(), name='videopages_page'),
    url(r'(?P<username>[\w]+)/$', UserVideoPageListView.as_view(), name='videopages_user_list'),
)
# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from videopages.views.become_publisher import BecomePublisherView
from videopages.views.feeds import LatestUsersVideosFeed, LatestUserVideosFeed
from videopages.views.tagcloud import VideoPageTagCloudView
from views.remove import remove_page
from views.create import create_page
from videopages.views.edit import EditVideoView
from videopages.views.list import VideoPageListView, UserVideoPageListView
from views.page import VideoPageView


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


urlpatterns = patterns('',
    url(r'^$', VideoPageListView.as_view(), name='videopages_list'),
    url(r'^rss/$', LatestUsersVideosFeed(), name='videopages_latest_users_videos'),
    url(r'^become_publisher/$', login_required(BecomePublisherView.as_view()), name='videopages_become_publisher'),
    url(r'^tag/(?P<tag>[^/]+)/$', VideoPageTagCloudView.as_view(), name='videopages_tagcloud'),
    url(r'^(?P<username>[\w\.]+)/rss/$', LatestUserVideosFeed(), name='videopages_latest_user_videos'),
    url(r'^(?P<username>[\w\.]+)/edit/(?P<slug>[\w-]+)/$',
        permission_required('djangovideos.add_video')(
            permission_required('videopages.add_videopage')(login_required(EditVideoView.as_view()))
        ),
        name='videopages_edit'),
    url(r'^(?P<username>[\w\.]+)/create/$',
        permission_required('djangovideos.add_video')(
            permission_required('videopages.add_videopage')(login_required(create_page))
        ),
        name='videopages_create'),
    url(r'^(?P<username>[\w\.]+)/remove/(?P<slug>[\w-]+)/$',
        permission_required('videopages.remove_videopage')(login_required(remove_page)),
        name='videopages_remove'),
    url(r'^(?P<username>[\w\.]+)/video/(?P<url>.*)$', VideoPageView.as_view(), name='videopages_page'),
    url(r'^(?P<username>[\w\.]+)/(?P<url>.*)/$', VideoPageView.as_view(), name='videopages_page'),
    url(r'(?P<username>[\w\.]+)/$', UserVideoPageListView.as_view(), name='videopages_user_list'),
)
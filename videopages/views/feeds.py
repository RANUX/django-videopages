# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from videopages.models import VideoPage

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class LatestUsersVideosFeed(Feed):
    title = _("Latest users videos")
    link = "/rss/"
    description = _("Updates on adding new videos by users")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def items(self):
        return VideoPage.not_removed_objects.latest_videos_filter()


class LatestUserVideosFeed(Feed):

    def get_object(self, request, username):
        return get_object_or_404(User, username=username)

    def title(self, obj):
        return "%s %s" % (_("Latest published videos by"), obj.username)

    def description(self, obj):
        return "%s %s" % (_("Updates on adding new videos by"), obj.username)

    def link(self, obj):
        return obj.get_absolute_url()

    def items(self, obj):
        return VideoPage.not_removed_objects.latest_videos_filter(author=obj)
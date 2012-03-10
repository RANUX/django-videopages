# -*- coding: UTF-8 -*-
from django.db import models
from django.db.models.query_utils import Q
from videopages.conf.settings import LATEST_VIDEOS_LIMIT

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class NotRemovedVideoPageManager(models.Manager):

    def get_query_set(self):
        return super(NotRemovedVideoPageManager, self).get_query_set().filter(removed=False)

    def latest_videos_filter(self, *args, **kwargs):
        return self.filter(**kwargs).exclude(Q(title__exact='')|Q(slug__exact='')).order_by('-created')[:LATEST_VIDEOS_LIMIT]


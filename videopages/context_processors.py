# -*- coding: UTF-8 -*-
from django.db.models.query_utils import Q
from conf.settings import LATEST_VIDEOS_LIMIT
from models import VideoPage
from conf.settings import CACHE_TIMEOUT


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


def latest_users_videos(request):
    result = VideoPage.not_removed_objects.latest_videos_filter()
    return {'latest_users_videos': result}

def cache_settings(request):
    return {'CACHE_TIMEOUT' : CACHE_TIMEOUT}
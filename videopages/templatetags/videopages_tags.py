# -*- coding: UTF-8 -*-
from django import template
from django.contrib.comments.models import Comment
from django.contrib.sites.models import Site
from videopages.conf.settings import CACHE_TIMEOUT
from videopages.models import VideoPage

register = template.Library()


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


@register.simple_tag(takes_context=True)
def get_latest_users_videos(context):
    result = VideoPage.not_removed_objects.latest_videos_filter()
    context['latest_users_videos'] = result
    return ''

@register.simple_tag(takes_context=True)
def get_CACHE_TIMEOUT(context):
    context['CACHE_TIMEOUT'] = CACHE_TIMEOUT
    return ''
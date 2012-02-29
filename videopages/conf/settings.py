# -*- coding: UTF-8 -*-
from django.conf import settings


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


LANGUAGES = getattr(settings, 'LANGUAGES')
VIDEO_PAGES_PER_PAGE = getattr(settings, 'VIDEO_PAGES_PER_PAGE', 10)
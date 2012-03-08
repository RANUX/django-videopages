# -*- coding: UTF-8 -*-
from django.conf import settings


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


LANGUAGES = getattr(settings, 'LANGUAGES')
VIDEO_PAGES_PER_PAGE = getattr(settings, 'VIDEO_PAGES_PER_PAGE', 5)
THUMBNAIL_PATH = getattr(settings, 'VIDEO_PAGES_THUMBNAIL_PATH', 'catalogs/icons/')
THUMBNAIL_WIDTH = getattr(settings, 'VIDEO_PAGES_THUMBNAIL_WIDTH', 160)
THUMBNAIL_HEIGHT = getattr(settings, 'VIDEO_PAGES_THUMBNAIL_HEIGHT', 80)
THUMBNAIL_CROP_TYPE = getattr(settings, 'VIDEO_PAGES_THUMBNAIL_CROP_TYPE', 'smart')
RANDOM_SLUG_LENGTH = getattr(settings, 'VIDEO_PAGES_RANDOM_SLUG_LENGTH', 10)
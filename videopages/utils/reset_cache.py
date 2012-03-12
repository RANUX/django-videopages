# -*- coding: UTF-8 -*-
import hashlib
from django.core.cache import cache
from django.utils.http import urlquote


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


def invalidate_template_cache(fragment_name, *variables):
    args = hashlib.md5(u':'.join([urlquote(var) for var in variables]))
    cache_key = 'template.cache.%s.%s' % (fragment_name, args.hexdigest())
    cache.delete(cache_key)

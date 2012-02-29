# -*- coding: UTF-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


####################################################################
# Paginator shortcuts
####################################################################

def create_paginated_page(query_set, page_number=1, objects_per_page=20):

    paginator = Paginator(query_set, objects_per_page)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)
    return page
# -*- coding: UTF-8 -*-
import urllib
from django.shortcuts import get_object_or_404
from tagging.models import Tag, TaggedItem
from django.views.generic.base import TemplateView
from videopages.conf.settings import VIDEO_PAGES_PER_PAGE
from videopages.models import VideoPage
from videopages.shortcuts import create_paginated_page

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageTagCloudView(TemplateView):
    template_name = 'videopages/list.html'

    def get(self, request, tag):
        tag = urllib.unquote(unicode(tag))
        tag = get_object_or_404(Tag, name=tag)
        videopages = TaggedItem.objects.get_by_model(VideoPage, tag)
        objects_page = create_paginated_page(
            query_set=videopages.filter(removed=False).order_by('-id'),
            page_number=request.GET.get('page') or 1,
            objects_per_page=VIDEO_PAGES_PER_PAGE
        )
        return self.render_to_response({'objects_page': objects_page })
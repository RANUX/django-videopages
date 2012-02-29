# -*- coding: UTF-8 -*-
from django.views.generic.base import TemplateView
from videopages.conf.settings import VIDEO_PAGES_PER_PAGE
from videopages.models import VideoPage
from videopages.shortcuts import create_paginated_page

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageListView(TemplateView):
    template_name = 'videopages/list.html'

    def get(self, request):
        objects_page = create_paginated_page(
            query_set=VideoPage.objects.all().order_by('-id'),
            page_number=request.GET.get('page') or 1,
            objects_per_page=VIDEO_PAGES_PER_PAGE
        )
        return self.render_to_response({'objects_page': objects_page })
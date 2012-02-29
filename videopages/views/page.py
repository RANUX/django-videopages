# -*- coding: UTF-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from videopages.models import VideoPage

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageView(TemplateView):
    template_name = 'videopages/page.html'


    def get(self, request, *args, **kwargs):
        url = kwargs.get('url')

        if url:
            if not url.endswith('/'):
                return HttpResponseRedirect("%s/" % request.path)

            slug = filter(None, url.split("/"))[-1]  # filter removes empty strings
            videopage = get_object_or_404(VideoPage, slug=slug, deleted=False)

        return self.render_to_response({'videopage': videopage})
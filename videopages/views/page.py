# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from videopages.models import VideoPage

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageView(TemplateView):
    template_name = 'videopages/page.html'


    def get(self, request, username, url, *args, **kwargs):

        author = get_object_or_404(User, username=username)
        slug = filter(None, url.split("/"))[-1]  # filter removes empty strings
        videopage = get_object_or_404(VideoPage, removed=False, slug=slug, author=author)

        return self.render_to_response({'videopage': videopage})
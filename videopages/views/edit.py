# -*- coding: UTF-8 -*-
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView
from djangovideos.models import Video
from videopages.forms.page import VideoPageForm
from videopages.models import VideoPage

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class EditVideoView(TemplateView):
    template_name = 'videopages/edit.html'

    def get(self, request, *args, **kwargs):
        videopage = get_object_or_404(VideoPage, author=request.user, slug=kwargs.get('slug'))
        videopage_form = VideoPageForm(instance=videopage)
        return self.render_to_response({'videopage': videopage, 'videopage_form': videopage_form})

    def post(self, request, *args, **kwargs):
        videopage = get_object_or_404(VideoPage, author=request.user, slug=kwargs.get('slug'))
        videopage_form = VideoPageForm(request.POST, instance=videopage)
        if videopage_form.is_valid():
            videopage_form.save()
            return redirect('videopages_edit', videopage.slug)
        else:
            videopage_form = VideoPageForm(instance=videopage)
        return self.render_to_response({'videopage': videopage, 'videopage_form': videopage_form})
# -*- coding: UTF-8 -*-
import random
import string
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from djangovideos.models import Video
from videopages.conf.settings import RANDOM_SLUG_LENGTH
from videopages.forms.page import VideoPageForm
from videopages.models import VideoPage


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class EditVideoView(TemplateView):
    template_name = 'videopages/edit.html'

    def get(self, request, username, *args, **kwargs):
        slug=kwargs.get("slug")

        if not slug:
            slug = ''.join(random.choice(string.letters) for i in xrange(RANDOM_SLUG_LENGTH))

        videopage, created = VideoPage.objects.get_or_create(
            author=request.user,
            slug=slug,
            defaults={
                'author': request.user,
                'slug': slug,
            }
        )
        videopage_form = VideoPageForm(instance=videopage)
        return self.render_to_response({'videopage': videopage, 'videopage_form': videopage_form})

    def post(self, request, username, slug, *args, **kwargs):
        videopage = get_object_or_404(VideoPage, author=request.user, slug=slug)
        videopage_form = VideoPageForm(request.POST, instance=videopage)
        if videopage_form.is_valid():
            videopage_form.save()
            messages.info(request, _("Video page saved successfully"))
            return redirect('videopages_edit', request.user.username, videopage.slug)
        else:
            videopage_form = VideoPageForm(instance=videopage)
        return self.render_to_response({'videopage': videopage, 'videopage_form': videopage_form})

# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from videopages.models import VideoPage


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


def create_page(request, username):
    video_page = VideoPage.objects.create(author=request.user, slug=VideoPage.objects.count())
    return redirect('videopages_edit', request.user.username, video_page.slug)

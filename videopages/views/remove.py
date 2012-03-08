# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from videopages.models import VideoPage


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


def remove_page(request, username, slug):
    videopage = get_object_or_404(VideoPage, author=request.user, slug=slug)
    videopage.removed = True
    videopage.save()
    messages.info(request, _("Video page removed successfully"))
    return redirect('videopages_user_list', username)
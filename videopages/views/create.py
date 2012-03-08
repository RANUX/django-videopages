# -*- coding: UTF-8 -*-
import random
import string
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from videopages.conf.settings import RANDOM_SLUG_LENGTH
from videopages.models import VideoPage


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


def create_page(request, username):
    slug = ''.join(random.choice(string.letters) for i in xrange(RANDOM_SLUG_LENGTH))
    videopage = VideoPage.objects.create(author=request.user, slug=slug)
    messages.info(request, _("Video page created successfully"))
    return redirect('videopages_edit', request.user.username, videopage.slug)
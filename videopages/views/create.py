# -*- coding: UTF-8 -*-
import random
import string
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query_utils import Q
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from djangovideos.models import Video
from videopages.conf.settings import RANDOM_SLUG_LENGTH
from videopages.models import VideoPage


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


def create_page(request, username):
    videopage_ctype = ContentType.objects.get(app_label="videopages", model="videopage")
    inner_q = Video.objects.filter(content_type=videopage_ctype).values('object_id').query

    try:
        # find videopage whithout video or title
        videopage = VideoPage.not_removed_objects.get(Q(author=request.user) & (Q(title='') | ~Q(pk__in=inner_q)))
        messages.info(request, _("Finish existing video page"))
    except ObjectDoesNotExist:
        slug = ''.join(random.choice(string.letters) for i in xrange(RANDOM_SLUG_LENGTH))
        videopage = VideoPage.objects.create(author=request.user, slug=slug)
        messages.info(request, _("Video page created successfully"))

    return redirect('videopages_edit', request.user.username, videopage.slug)
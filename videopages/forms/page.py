# -*- coding: UTF-8 -*-
from django import forms
from videopages.models import VideoPage


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageForm(forms.ModelForm):

    class Meta:
        model = VideoPage
        fields = ('title', 'description', 'thumbnail', 'thumbnail_url', 'slug', 'tags', 'language_code')
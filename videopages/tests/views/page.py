# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from videopages.models import VideoPage
from videopages.tests.views.base import BaseTestCase


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageViewTestCase(BaseTestCase):
    fixtures = [
        'videopages_videopages.json'
    ]

    def test_get_page(self):
        video_page = VideoPage.objects.get(pk=2)
        url = '{0}/'.format(reverse('videopages_page', args=[self.user.username, video_page.slug]))
        response = self.client.get(url)
        for item in [video_page.title, video_page.description]:
            self.assertContains(response, item)


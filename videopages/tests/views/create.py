# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse
from base import BaseTestCase
from videopages.models import VideoPage

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageTestCase(BaseTestCase):

    def test_create(self):
        self.assertEquals(0, VideoPage.objects.count())
        url = reverse("videopages_create")
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 302)
        self.assertEquals(1, VideoPage.objects.count())
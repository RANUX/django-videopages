# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse
from videopages.models import VideoPage
from base import BaseTestCase

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageTestCase(BaseTestCase):
    fixtures = [
        "catalogs.json",
        "videopages.json"
    ]

    def test_create_and_edit(self):
        page_slug = VideoPage.objects.all().order_by('-id')[0].slug
        url = reverse("videopages_edit", kwargs={"slug": page_slug})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

        data = {
            "tags": u"lesson",
            "name": u"lesson 9",
            "slug": u"lesson-9",
            "description": u"test lesson"
        }
        url = reverse("videopages_edit", kwargs={"slug": page_slug})
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse("videopages_edit", kwargs={"slug": "lesson-9"})+u"?")

        url = reverse("videopages_edit", kwargs={"slug": "lesson-9"})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
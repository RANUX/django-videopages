# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse
from videopages.models import VideoPage
from base import BaseTestCase

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageTestCase(BaseTestCase):
    fixtures = [
        "videopages_videopages.json"
    ]

    def test_create_and_edit(self):
        self.set_edit_video_user_permissions()
        page_slug = VideoPage.objects.all().order_by('-id')[0].slug
        url = reverse("videopages_edit", args=[self.user.username, page_slug])
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

        data = {
            "tags": u"lesson",
            "title": u"lesson 9",
            "slug": u"awesom-lesson",
            "description": u"test lesson",
            "language_code": u"en",
        }
        url = reverse("videopages_edit", args=[self.user.username, page_slug])
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse("videopages_edit", args=[self.user.username, data['slug']]))

        url = reverse("videopages_edit", args=[self.user.username, data['slug']])
        response = self.client.get(url)
        for key in data.keys():
            self.assertContains(response, data[key])

        self.failUnlessEqual(response.status_code, 200)
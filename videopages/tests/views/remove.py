# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse
from base import BaseTestCase
from videopages.models import VideoPage


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageTestCase(BaseTestCase):

    def test_remove(self):
        self.set_edit_video_user_permissions()
        url = reverse("videopages_create", args=[self.user.username])
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 302)
        videopage = VideoPage.objects.filter(removed=False)[0]

        self.set_remove_video_user_permissions()
        url = reverse("videopages_remove", args=[self.user.username, videopage.slug])
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 302)
        self.assertEquals(0, VideoPage.not_removed_objects.count())
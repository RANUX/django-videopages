# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse
from base import BaseTestCase
from videopages.models import VideoPage

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageTestCase(BaseTestCase):

    def test_create(self):
        self.set_edit_video_user_permissions()
        self.assertEquals(0, VideoPage.objects.count())
        response = self.create_new()
        self.failUnlessEqual(response.status_code, 302)
        self.assertEquals(1, VideoPage.objects.count())

    def test_redirect_to_incomplete_page(self):
        self.set_edit_video_user_permissions()
        response = self.create_new()
        videopage = VideoPage.objects.all().order_by('-id')[0]
        videopage.title='this is test'
        videopage.save()

        response = self.create_new()
        self.assertEquals(1, VideoPage.objects.count())
        self.assertEquals(videopage.id, VideoPage.objects.all().order_by('-id')[0].id)

    def create_new(self):
        url = reverse("videopages_create", args=[self.user.username])
        return self.client.post(url)
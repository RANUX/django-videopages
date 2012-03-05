# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse
from base import BaseTestCase

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageListViewTestCase(BaseTestCase):
    fixtures = [
        "videopages_videopages.json"
    ]

    def test_list(self):
        url = reverse("videopages_list")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
        self.assertIsNotNone(response.context[0].get('objects_page'))


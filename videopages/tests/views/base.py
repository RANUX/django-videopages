# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User, Permission
from django.test import TestCase


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class BaseTestCase(TestCase):
    def setUp(self):
        password = '12345'
        self.user = User.objects.create_user(
            'user',
            'user@example.com',
            password,
        )
        is_logged = self.client.login(username=self.user.username, password=password)
        self.assertTrue(is_logged)

    def set_edit_video_user_permissions(self):
        self.user.user_permissions.add(Permission.objects.get(codename='add_video'))
        self.user.user_permissions.add(Permission.objects.get(codename='add_videopage'))
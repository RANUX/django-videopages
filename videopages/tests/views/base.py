# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
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
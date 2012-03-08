# -*- coding: UTF-8 -*-
from django.db import models

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class NotRemovedVideoPageManager(models.Manager):

    def get_query_set(self):
        return super(NotRemovedVideoPageManager, self).get_query_set().filter(removed=False)


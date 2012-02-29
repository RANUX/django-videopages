# -*- coding: UTF-8 -*-
from catalogs.models import CatalogItem
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

class VideoPage(CatalogItem):

    author = models.ForeignKey(User, related_name="videos", verbose_name=_('author'))

    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    description = models.TextField(verbose_name=_('description'))
    tags = TagField(verbose_name=_('tags'), blank=True)
    moderated = models.BooleanField(_('moderated'), default=False)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'{0} - {1}'.format(self.author.username, self.slug)

    def get_absolute_url(self):
        return reverse('videopages_page', args=[self.slug])

# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField
from conf.settings import LANGUAGES

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

class VideoPage(models.Model):

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'))
    author = models.ForeignKey(User, related_name="videos", verbose_name=_('author'))
    published = models.BooleanField(_('published'), default=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    description = models.TextField(verbose_name=_('description'), blank=True)
    tags = TagField(verbose_name=_('tags'), blank=True)

    language_code = models.CharField(_('language'), max_length=8, choices=LANGUAGES, default=dict(LANGUAGES).keys()[0])

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'{0} - {1}'.format(self.author.username, self.slug)

    def get_absolute_url(self):
        return reverse('videopages_page', args=[self.slug])

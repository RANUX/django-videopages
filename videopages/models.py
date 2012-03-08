# -*- coding: UTF-8 -*-
import os
import urllib
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files.base import File
from django.db import models
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField
from easy_thumbnails.fields import ThumbnailerImageField
from conf.settings import LANGUAGES, THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT, THUMBNAIL_CROP_TYPE, THUMBNAIL_PATH
from managers import NotRemovedVideoPageManager

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

class VideoPage(models.Model):

    THUMBNAIL_SETTINGS = {
        'size': (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT),
        'crop': THUMBNAIL_CROP_TYPE
    }

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'))
    author = models.ForeignKey(User, related_name="videos", verbose_name=_('author'))
    published = models.BooleanField(_('published'), default=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    description = models.TextField(verbose_name=_('description'), blank=True)
    tags = TagField(verbose_name=_('tags'), blank=True)
    removed = models.BooleanField(_('removed'), default=False)
    thumbnail_url = models.URLField(_('thumbnail url'), blank=True)
    thumbnail = ThumbnailerImageField(
        _('thumbnail'),
        blank=True,
        upload_to=THUMBNAIL_PATH,
        resize_source=THUMBNAIL_SETTINGS
    )

    objects = models.Manager()
    not_removed_objects = NotRemovedVideoPageManager()

    language_code = models.CharField(_('language'), max_length=8, choices=LANGUAGES, default=dict(LANGUAGES).keys()[0])

    def save(self, *args, **kwargs):
        super(VideoPage, self).save(*args, **kwargs)
        self.store_thumbnail_by_url()


    def store_thumbnail_by_url(self):
        """Store thumbnail locally if we have an URL"""
        if self.thumbnail_url and not self.thumbnail:

            result = urllib.urlretrieve(self.thumbnail_url)
            self.thumbnail.save(
                os.path.basename(self.thumbnail_url),
                File(open(result[0]))
            )
            self.save()

    class Meta:
        ordering = ['-created']
        permissions = (
            ("remove_videopage", "Can remove videopage"),
        )

    def __unicode__(self):
        return u'{0} - {1}'.format(self.author.username, self.slug)

    def get_absolute_url(self):
        return reverse('videopages_page', args=[self.slug])

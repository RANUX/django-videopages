# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class BecomePublisherView(TemplateView):
    template_name = 'videopages/become_publisher.html'

    def get(self, request, *args, **kwargs):
        g = Group.objects.get(name='publishers')
        request.user.groups.add(g)
        messages.info(request, _("You became a publisher"))
        return self.render_to_response({})
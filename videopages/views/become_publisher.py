# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class BecomePublisherView(TemplateView):
    template_name = 'videopages/publisher_terms.html'

    def post(self, request):
        g = Group.objects.get(name='publishers')
        request.user.groups.add(g)
        messages.info(request, _("Now you can publish videos"))
        return redirect('videopages_user_list', request.user.username)
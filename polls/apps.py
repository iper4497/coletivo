# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'
    verbose_name = _('polls')

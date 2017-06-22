# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from spaces.models import Space
from profiles.models import Profile


class Task(models.Model):
    name = models.CharField(_('name'), max_length=254)
    assign = models.ManyToManyField(Profile, blank=True,
        related_name=_('assign'))
    deadline = models.DateField(_('deadline'), null=True, blank=True)
    space = models.ForeignKey(Space, on_delete=models.CASCADE,
        related_name=('space'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')
        ordering = ["-deadline"]

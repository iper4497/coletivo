# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profiles.models import Profile


class Task(models.Model):
    name = models.CharField(max_length=254)
    assign = models.ManyToManyField(Profile, blank=True)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-deadline"]

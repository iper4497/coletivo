# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from spaces.models import Space
from django.db import models


class Question(models.Model):
    question_text = models.CharField(_('question text'), max_length=254)
    pub_date = models.DateTimeField(_('publication date'))
    space = models.ForeignKey(Space, on_delete=models.CASCADE,
        related_name=_('space'))

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
        ordering = ["pub_date"]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
        related_name=_('question'))
    choice_text = models.CharField(_('choice text'), max_length=254)
    votes = models.IntegerField(_('votes'), default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = _('choice')
        verbose_name_plural = _('choices')
        ordering = ["question"]
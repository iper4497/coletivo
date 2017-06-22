# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
from profiles.models import Profile


class Tag(models.Model):
    word = models.CharField(_('word'), max_length=50)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class Space(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4,
            editable=False)
    name = models.CharField(_('name'), max_length=150)
    description = models.TextField(_('description'), null=True)
    # Join Policy: 0 - Required Invitation(default) -> 1 - Free Join
    POLICY = (
        ('0', _('Invitation')),
        ('1', _('Free')),
    )
    join_policy = models.CharField(_('join policy'), max_length=1,
         choices=POLICY)
    visibility = models.BooleanField(_('visibility'), default=True)
    tags = models.ManyToManyField(Tag, related_name=_('tags'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True,
        editable=False)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE,
        related_name=_('created_by'))
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    updated_by = models.ForeignKey(Profile, null=True,
        related_name=_('updated_by'))
    color = models.CharField(_('color'), max_length=20)
    url = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('space')
        verbose_name_plural = _('spaces')
        ordering = ['-created_at']

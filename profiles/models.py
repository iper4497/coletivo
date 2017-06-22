# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        related_name=_('user'))
    email_confirmed = models.BooleanField(_('email confirmed'), default=False)
    avatar = models.ImageField(_('avatar'), upload_to='profiles/', blank=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

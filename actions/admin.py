# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Action
from django.contrib import admin


class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)

admin.site.register(Action, ActionAdmin)

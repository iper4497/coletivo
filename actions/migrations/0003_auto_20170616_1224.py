# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_auto_20170616_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='target_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='target_obj', to='contenttypes.ContentType'),
        ),
    ]

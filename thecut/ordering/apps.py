# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import receivers
from django import apps
from django.db.models import signals


class AppConfig(apps.AppConfig):

    label = 'ordering'

    name = 'thecut.ordering'

    def ready(self):
        signals.post_init.connect(receivers.set_order)

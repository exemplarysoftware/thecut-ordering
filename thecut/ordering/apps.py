# -*- coding: utf-8 -*-


from django import apps
from django.db.models import signals

from . import receivers


class AppConfig(apps.AppConfig):

    label = "ordering"

    name = "thecut.ordering"

    def ready(self):
        signals.post_init.connect(receivers.set_order)

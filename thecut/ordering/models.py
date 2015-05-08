# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import receivers
from django.db import models


class OrderMixin(models.Model):

    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        abstract = True
        ordering = ['order', 'pk']

models.signals.post_init.connect(receivers.set_order)

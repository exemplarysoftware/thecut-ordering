# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from thecut.ordering import receivers


class OrderMixin(models.Model):

    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        abstract = True
        ordering = ('order',)

models.signals.post_init.connect(receivers.set_order)
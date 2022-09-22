# -*- coding: utf-8 -*-


from django.db import models


class OrderMixin(models.Model):

    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        abstract = True
        ordering = ["order", "pk"]

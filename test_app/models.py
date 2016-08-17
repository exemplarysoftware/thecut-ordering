# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.ordering.models import OrderMixin
from django.db import models


class OrderingTestModel(OrderMixin, models.Model):
    # A class to provide useful testing of the ordermixin

    #title = models.CharField()
    pass



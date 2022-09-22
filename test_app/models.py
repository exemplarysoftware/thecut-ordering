# -*- coding: utf-8 -*-


from django.db import models

from thecut.ordering.models import OrderMixin


class OrderingTestModel(OrderMixin, models.Model):
    # A class to provide useful testing of the ordermixin
    pass

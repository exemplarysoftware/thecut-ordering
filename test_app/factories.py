# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .models import OrderingTestModel

try:
    import factory
except ImportError as error:
    message = '{0}. Try running `pip install factory_boy`.'.format(error)
    raise ImportError(message)


class OrderingTestModelFactory(factory.django.DjangoModelFactory):

    class Meta(object):
        model = OrderingTestModel


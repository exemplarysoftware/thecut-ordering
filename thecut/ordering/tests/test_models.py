# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from django import VERSION as DJANGO_VERSION
from test_app.factories import OrderingTestModelFactory
from test_app.models import OrderingTestModel
from unittest import skipIf


class TestAuthorshipModel(TestCase):

    def test_the_order_is_the_default_order_of_query(self):
        ordertest1 = OrderingTestModelFactory.build()
        ordertest1.save()
        self.assertEqual(ordertest1.pk, 1)

        ordertest2 = OrderingTestModelFactory.build()
        ordertest2.save()
        self.assertEqual(ordertest2.pk, 2)

        ordertest1.order = 2
        ordertest2.order = 1
        ordertest1.save()
        ordertest2.save()

        ordertests = OrderingTestModel.objects.all()

        self.assertEqual(len(ordertests), 2)
        self.assertEqual(ordertests[0].pk, 2)
        self.assertEqual(ordertests[0].order, 1)
        self.assertEqual(ordertests[1].pk, 1)
        self.assertEqual(ordertests[1].order, 2)


    def test_new_models_are_appended_to_the_end(self):
        ordertest1 = OrderingTestModelFactory.build()
        ordertest1.pk = 3
        ordertest1.save()

        ordertest2 = OrderingTestModelFactory.build()
        ordertest2.pk = 2
        ordertest2.save()

        ordertests = OrderingTestModel.objects.all()

        self.assertEqual(len(ordertests), 2)
        self.assertEqual(ordertests[0].pk, 3)
        self.assertEqual(ordertests[1].pk, 2)


    def test_the_pk_is_used_as_the_secondary_order(self):
        ordertest1 = OrderingTestModelFactory.build()
        ordertest1.save()
        self.assertEqual(ordertest1.pk, 1)

        ordertest2 = OrderingTestModelFactory.build()
        ordertest2.save()
        self.assertEqual(ordertest2.pk, 2)

        ordertest1.order = 1
        ordertest2.order = 1
        ordertest1.save()
        ordertest2.save()

        ordertests = OrderingTestModel.objects.all()

        self.assertEqual(len(ordertests), 2)
        self.assertEqual(ordertests[0].pk, 1)
        self.assertEqual(ordertests[0].order, 1)
        self.assertEqual(ordertests[1].pk, 2)
        self.assertEqual(ordertests[1].order, 1)


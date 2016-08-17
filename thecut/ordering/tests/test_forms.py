# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from test_app.factories import OrderingTestModelFactory
from test_app.forms import OrderingTestNoOrderFieldForm
from test_app.forms import OrderingTestHasOrderFieldForm


class TestOrderingForms(TestCase):

    def test_ordering_form_mixin_with_no_ordering_field(self):
        ordertest1 = OrderingTestModelFactory.build()
        ordertest1.save()
        form = OrderingTestNoOrderFieldForm(instance=ordertest1)

        self.assertTrue('order' not in form.fields)

    def test_ordering_form_mixin_with_ordering_field(self):
        ordertest1 = OrderingTestModelFactory.build()
        ordertest1.save()
        form = OrderingTestHasOrderFieldForm(instance=ordertest1)

        self.assertTrue('order' in form.fields)
        self.assertEqual(form.fields['order'].initial, ordertest1.order)

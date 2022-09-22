# -*- coding: utf-8 -*-


from django.forms import ModelForm

from thecut.ordering.forms import OrderMixin

from .models import OrderingTestModel


class OrderingTestNoOrderFieldForm(OrderMixin, ModelForm):
    # A class to provide useful testing of the ordermixin
    class Meta:
        model = OrderingTestModel
        fields = ["id"]


class OrderingTestHasOrderFieldForm(OrderMixin, ModelForm):
    # A class to provide useful testing of the ordermixin
    class Meta:
        model = OrderingTestModel
        fields = ["id", "order"]

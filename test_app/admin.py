# -*- coding: utf-8 -*-


from django.contrib import admin

from thecut.ordering.admin import ReorderMixin

from .models import OrderingTestModel


@admin.register(OrderingTestModel)
class OrderingTestModelAdmin(ReorderMixin, admin.ModelAdmin):

    model = OrderingTestModel
    ordering = ("order",)

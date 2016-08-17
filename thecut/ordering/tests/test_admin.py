# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from django import VERSION as DJANGO_VERSION
from test_app.factories import OrderingTestModelFactory
from test_app.models import OrderingTestModel
from test_app.forms import OrderingTestNoOrderFieldForm, OrderingTestHasOrderFieldForm
from unittest import skipIf
import thecut.ordering.models
from django.db import models
from test_app.factories import OrderingTestModelFactory
from test_app.admin import OrderingTestModelAdmin
from test_app.models import OrderingTestModel
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User, Permission
from django.core.urlresolvers import reverse
from test_app.urls import urlpatterns


class TestOrderingViews(TestCase):
    def setUp(self):
        super(TestOrderingViews, self).setUp()
        # Create an admin user.
        self.admin_user = User.objects.create_user(
            'admin', 'a@a.com', 'adminpass')
        self.admin_user.is_superuser = True
        self.admin_user.save()

        # Create a staff user.
        self.staff_user = User.objects.create_user(
            'staff', 'a@a.com', 'staffpass')
        self.staff_user.is_staff = True
        self.staff_user.save()

        # Create a non-admin user.
        self.user = User.objects.create_user(
            'user', 'a@a.com', 'userpass')

    def test_model_admin_using_the_OrderMixin(self):
        site = AdminSite()
        admin = OrderingTestModelAdmin(OrderingTestModel, site)
        urls = admin.get_urls()
        urls = [url for url in urls if url.name == 'reorder']
        self.assertEqual(len(urls), 1)


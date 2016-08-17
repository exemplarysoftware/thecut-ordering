# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase, RequestFactory
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
from thecut.ordering.views import AdminReorderView
from django.http import HttpResponseForbidden
from django.contrib.contenttypes.models import ContentType


class TestSecurityOrderingViews(TestCase):
    def setUp(self):
        super(TestSecurityOrderingViews, self).setUp()
        # Create an admin user.
        self.admin_user = User.objects.create_user(
            'admin', 'a@a.com', 'adminpass')
        self.admin_user.is_superuser = True
        self.admin_user.save()

        # Create a staff user.
        self.staff_user = User.objects.create_user(
            'staff', 'a@a.com', 'staffpass')
        content_type = ContentType.objects.get_for_model(OrderingTestModel)
        permission = Permission.objects.get(codename='change_orderingtestmodel',
                                            content_type=content_type)
        self.staff_user.user_permissions.add(permission)
        self.staff_user.is_staff = True
        self.staff_user.save()

        # Create a non-admin user.
        self.user = User.objects.create_user(
            'user', 'a@a.com', 'userpass')

        self.factory = RequestFactory()

    def test_view_rejects_ordinary_user(self):
        request = self.factory.post('')

        request.user = self.user

        site = AdminSite()
        admin = OrderingTestModelAdmin(OrderingTestModel, site)
        response = AdminReorderView.as_view()(request, admin=admin)

        self.assertEqual(response.status_code,
                         HttpResponseForbidden.status_code)

    def test_view_accepts_superuser(self):
        request = self.factory.post('')

        request.user = self.admin_user

        site = AdminSite()
        admin = OrderingTestModelAdmin(OrderingTestModel, site)
        response = AdminReorderView.as_view()(request, admin=admin)

        self.assertEqual(response.status_code, 200)

    def test_view_accepts_staffuser_with_permission(self):
        request = self.factory.post('')

        request.user = self.staff_user

        site = AdminSite()
        admin = OrderingTestModelAdmin(OrderingTestModel, site)
        response = AdminReorderView.as_view()(request, admin=admin)

        self.assertEqual(response.status_code, 200)


class TestReorderingOrderingViews(TestCase):
    def setUp(self):
        super(TestReorderingOrderingViews, self).setUp()
        # Create an admin user.
        self.admin_user = User.objects.create_user(
            'admin', 'a@a.com', 'adminpass')
        self.admin_user.is_superuser = True
        self.admin_user.save()

        self.factory = RequestFactory()

    def test_view_accepts_superuser(self):
        ordertest1 = OrderingTestModelFactory.build()
        ordertest1.save()
        ordertest2 = OrderingTestModelFactory.build()
        ordertest2.save()
        request = self.factory.post('', {'pk':[ordertest2.pk,ordertest1.pk]})

        request.user = self.admin_user

        site = AdminSite()
        admin = OrderingTestModelAdmin(OrderingTestModel, site)
        response = AdminReorderView.as_view()(request, admin=admin)

        self.assertEqual(response.status_code, 200)

        ordertests = OrderingTestModel.objects.all()

        self.assertEqual(len(ordertests), 2)
        self.assertEqual(ordertests[0].pk, ordertest2.pk)
        self.assertEqual(ordertests[1].pk, ordertest1.pk)


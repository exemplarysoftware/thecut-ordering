# -*- coding: utf-8 -*-


import sys

from django.urls import path

from .views import AdminReorderView


class ReorderMixin(object):

    list_per_page = sys.maxsize

    class Media(object):
        css = {"screen": ["ordering/admin-changelist-ordering.css"]}
        js = [
            "ordering/jquery.js",
            "ordering/jquery-ui.js",
            "ordering/jquery.init.js",
            "ordering/csrf.js",
            "ordering/admin-changelist-ordering.js",
        ]

    def get_urls(self):
        urlpatterns = [
            path(
                "reorder",
                AdminReorderView.as_view(),
                kwargs={"admin": self},
                name="reorder",
            ),
        ]
        urlpatterns += super(ReorderMixin, self).get_urls()
        return urlpatterns

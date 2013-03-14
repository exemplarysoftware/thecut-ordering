# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls.defaults import url, patterns
from thecut.ordering.views import AdminReorderView


class ReorderMixin(object):

    class Media(object):
        css = {'screen': ['ordering/admin-changelist-ordering.css']}
        js = ['ordering/jquery.js', 'ordering/jquery-ui.js',
              'ordering/jquery.init.js', 'ordering/csrf.js',
              'ordering/admin-changelist-ordering.js']

    def get_urls(self):
        urlpatterns = patterns('thecut.ordering.views',
            url(r'^reorder$', AdminReorderView.as_view(),
                kwargs={'admin': self}, name='reorder'),
        )
        urlpatterns += super(ReorderMixin, self).get_urls()
        return urlpatterns

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class OrderMixin(object):
    """Mixin for a form to set initial data for publish_at and site is set."""

    def __init__(self, *args, **kwargs):
        super(OrderMixin, self).__init__(*args, **kwargs)
        # Ensure initial order value matches instance (after it's post-init)
        if self.fields.get('order', False):
            self.fields['order'].initial = self.instance.order

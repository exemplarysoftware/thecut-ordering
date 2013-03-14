# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class OrderFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(OrderFormMixin, self).__init__(*args, **kwargs)
        # Ensure initial order value matches instance (after it's post-init)
        if self.fields.get('order', False):
            self.fields['order'].initial = self.instance.order

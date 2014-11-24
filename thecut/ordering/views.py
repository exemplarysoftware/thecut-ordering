# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic.list import MultipleObjectMixin


class BaseReorderView(MultipleObjectMixin, generic.View):
    """View for setting order on a list of objects.

    Currently only intended for AJAX POST requests, where an ordered list of
    ``pk`` key/values are included in the request body.

    :example: pk=5&pk=3&pk=1

    """

    order_field = 'order'

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(BaseReorderView, self).dispatch(*args, **kwargs)

    def get_order_field(self):
        return self.order_field

    def post(self, *args, **kwargs):
        ordered_pks = self.request.POST.getlist('pk')
        self.set_order(ordered_pks)
        return HttpResponse(content_type='text/plain')

    def set_order(self, ordered_pks):
        """Update the order field value for each item in ``ordered_pks``.

        :param ordered_pks: An ordered list of primary keys.
        :type ordered_pks: list

        """

        order_field = self.get_order_field()
        queryset = self.get_queryset()

        for pk in ordered_pks:
            opts = {order_field: ordered_pks.index(pk) + 1}
            queryset.filter(pk=pk).update(**opts)


class AdminReorderView(BaseReorderView):

    def dispatch(self, request, *args, **kwargs):
        # Set queryset, and check for 'change' permissions
        self.admin = kwargs['admin']
        self.queryset = self.admin.queryset(request)
        model = self.admin.model
        permission = '%s.change_%s' % (model._meta.app_label.lower(),
                                       model._meta.object_name.lower())
        if not request.user.has_perm(permission):
            return HttpResponseForbidden(content_type='text/plain')
        return super(AdminReorderView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset

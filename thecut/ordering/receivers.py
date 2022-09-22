# -*- coding: utf-8 -*-


from django.db.models import Max


def set_order(sender, instance, **kwargs):
    """If not set, determine and set the instance's order value."""
    from .models import OrderMixin

    is_order_subclass = issubclass(instance.__class__, OrderMixin)
    raw = kwargs.get("raw", False)

    if is_order_subclass and not any([instance.pk, instance.order, raw]):
        order = instance.__class__.objects.aggregate(order=Max("order")).get(
            "order"
        )
        instance.order = order + 1 if order is not None else 1

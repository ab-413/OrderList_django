from django import template
from crm.models import Order

register = template.Library()


@register.simple_tag
def order_count(id):
    return Order.objects.filter(customer=id).count()

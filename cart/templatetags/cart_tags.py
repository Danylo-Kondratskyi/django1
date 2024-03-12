from django.utils.http import urlencode

from cart.models import Cart
from cart.utils import get_user_carts
from goods.models import Category
from django import template

register = template.Library()


@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)
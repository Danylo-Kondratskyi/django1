from django.utils.http import urlencode

from cart.models import Cart
from goods.models import Category
from django import template

register = template.Library()


@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    else:
        return Cart.objects.none()
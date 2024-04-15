from django import template
import math
register = template.Library()

@register.simple_tag
def sel_price(price,discount):
    if discount is None or discount == 0:
        return price
    selprice = price - (price * discount*0.01)
    return math.floor(selprice)


@register.filter
def rupee(price):
    return f"₹{price}"
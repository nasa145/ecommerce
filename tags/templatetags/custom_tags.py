

from django import template
from shop.models import Category

register = template.Library()

@register.simple_tag
def categories():
    categories = Category.objects.all()
    return categories
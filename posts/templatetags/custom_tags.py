import random
from django import template

register = template.Library()


@register.simple_tag
def random_number(min=0, max=100):
    return random.randint(min, max)


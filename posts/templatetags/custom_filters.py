from django import template

register = template.Library()


@register.filter
def scream(value):
    return value.upper() + "!!!"
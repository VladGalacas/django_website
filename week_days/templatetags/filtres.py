from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key=' '):
    return value.split(key)

@register.filter(name='lower')
def lower(value):
    return value.lower()
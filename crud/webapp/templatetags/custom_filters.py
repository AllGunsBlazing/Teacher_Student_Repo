from django import template

register = template.Library()

@register.filter(name='startswith')
def startswith(value, arg):
    if not isinstance(value, str):
        return False
    return value.startswith(arg)
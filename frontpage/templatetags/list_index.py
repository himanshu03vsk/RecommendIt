from django import template

register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def nested_list(mul_list):
    if len(mul_list) == 1:
        return mul_list[0]
    return ", ".join(mul_list) 

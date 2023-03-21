from django import template

register = template.Library()

@register.filter(name="capitalize")
def capitalize(string: str):
    
    return string.capitalize()

# register.filter("capitalize", capitalize)
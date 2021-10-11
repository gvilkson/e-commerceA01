from django import template

register = template.Library()

@register.simple_tag
def model_name(value):
    '''
    Django template filter whitch returns the verbose name of a model.
    '''
    if hasattr(value, 'model'):
        value = value.model
        return value.meta.verbose_name.title()
    return('')


@register.simple_tag
def model_name_plural(value):
    '''
    Django template filter whitch returns the verbose name of a model.
    '''
    if hasattr(value, 'model'):
        value = value.model
        return value.meta.verbose_name_plural.title()
    return('')
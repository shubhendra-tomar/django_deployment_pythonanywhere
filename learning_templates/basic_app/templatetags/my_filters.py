from django import template

register = template.Library()

#register using decorator to register at time of creation
@register.filter(name = 'cuts')
def cuts(value, args):
    """
    This cuts out values of args from string.
    """
    return value.replace(args, '')

#older method explicitly registering after creation
# register.filter('cuts', cuts)
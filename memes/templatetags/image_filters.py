from base64 import b64encode

from django.template.library import Library
from magic import from_buffer

register = Library()


@register.filter
def make_src(data):
    mime = from_buffer(data, mime=True)
    encoded_data = b64encode(data).decode()

    return f'data:{mime};base64,{encoded_data}'


@register.filter
def is_exists(image):
    try:
        image.file
    except FileNotFoundError:
        return False

    return True

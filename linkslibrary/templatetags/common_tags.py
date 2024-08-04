from django import template
from ..models import Resource
register = template.Library()


@register.inclusion_tag('templatetags/resourse.html', takes_context=True)
def show_links_menu(context):
    menu_items = Resource.objects.order_by('order')[:5]
    return {
        "links_items": menu_items,
    }
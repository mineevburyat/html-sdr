from django import template
from ..models import Resource
register = template.Library()


@register.inclusion_tag('templatetags/links_list.html', takes_context=True)
def show_links_menu(context):
    links_items = Resource.objects.order_by('order')
    return {
        "links_items": links_items,
    }
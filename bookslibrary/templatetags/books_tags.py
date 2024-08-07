from django import template
from ..models import Book
register = template.Library()


@register.inclusion_tag('templatetags/books_list.html', takes_context=True)
def show_books_icon(context):
    books_items = Book.objects.all()[:4]
    return {
        "books_items": books_items,
    }
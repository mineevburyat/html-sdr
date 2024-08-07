from django.views.generic.detail import DetailView
from .models import Post

class ViewPost(DetailView):
    model = Post
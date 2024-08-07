from django.conf import settings
from django.db import models
from django.utils import timezone
# from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=200)
    

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog.views.ViewPost', args=[str(self.id)])
from django.contrib import admin
from .models import Resource

# Register your models here.
@admin.register(Resource)
class AdminResourse(admin.ModelAdmin):
    # ordering = 'order'
    pass
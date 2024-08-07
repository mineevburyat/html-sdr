# Generated by Django 5.0.1 on 2024-08-07 07:32

import django.utils.timezone
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('text', django_ckeditor_5.fields.CKEditor5Field(max_length=2000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
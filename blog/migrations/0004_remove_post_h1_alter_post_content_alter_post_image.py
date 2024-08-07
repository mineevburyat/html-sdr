# Generated by Django 5.0.1 on 2024-08-07 08:09

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_created_date_remove_post_published_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='h1',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog'),
        ),
    ]
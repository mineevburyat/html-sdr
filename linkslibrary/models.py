from django.db import models


class Resource(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
        verbose_name = 'ресурс'
        verbose_name_plural = 'ресурсы'
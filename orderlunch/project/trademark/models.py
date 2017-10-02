from django.db import models

class Trademark(models.Model):
    name    = models.CharField(max_length=200, db_index=True, verbose_name='Title')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Trademark'
        verbose_name_plural = 'Trademarks'
        index_together = [
            ['id']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('trademark.views.details', args=[self.id])

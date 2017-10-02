from django.db import models
from trademark.models import Trademark

class Product(models.Model):
    name      = models.CharField(max_length=200, db_index=True, verbose_name='Title')
    trademark = models.ForeignKey(Trademark, related_name='trademarks')
    price     = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Available')
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        index_together = [
            ['id']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product.views.details', args=[self.id])
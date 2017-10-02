from django.db import models

from product.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    customer = models.ForeignKey(User, related_name='customers')
    created  = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated  = models.DateTimeField(verbose_name='Updated', auto_now=True)
    paid     = models.BooleanField(verbose_name='Paid', default=False)
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
        

class OrderItem(models.Model):
    order    = models.ForeignKey(Order, related_name='items')
    product  = models.ForeignKey(Product, related_name='order_items')
    price    = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

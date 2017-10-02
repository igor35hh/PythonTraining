from django.contrib import admin

from .models import Order, OrderItem
from django.utils.html import format_html

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']
    
def OrderDetail(obj):
    from django.urls import reverse
    return format_html('<a href="{}">Overview</a>'.format(
        reverse('orders:AdminOrderDetail', args=[obj.id])
))

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'created', 'updated', 'paid', OrderDetail]

    list_filter = ['paid', 'created', 'updated']

    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

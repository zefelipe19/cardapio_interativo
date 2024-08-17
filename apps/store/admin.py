from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('id',)
    fields = ('order_id', 'product_id', 'unit_price', 'quantity')


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline, )
    list_display = ('costumer_name', 'total_amount', 'created_at', 'updated_at')
    list_display_links = ('costumer_name',)


admin.site.register(Order, OrderAdmin)
from django.contrib import admin
from .models import Category, Product, Order, OrderItem


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    readonly_fields = ('id',)
    fields = (
        ('category', 'title', 'is_active','image',),
        ('price', 'promotional_price', 'is_promo'),
        'description',
    )


class CategoryAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)

    list_display = ('title',)
    list_display_links = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active', 'is_promo', 'promotional_price')
    list_display_links = ('title',)
    list_editable = ('price','is_active', 'is_promo', 'promotional_price')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('id',)
    fields = ('order', 'product', 'unit_price', 'quantity')


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline, )
    list_display = ('costumer_name', 'total_amount', 'created_at')
    list_display_links = ('costumer_name',)


admin.site.register(Order, OrderAdmin)

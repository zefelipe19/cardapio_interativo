from django.db import models
from ..menu.models import BaseModel, Product

class Order(BaseModel):
    costumer_name = models.CharField(max_length=255, verbose_name='Cliente')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total', blank=True, null=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'Pedido de {self.costumer_name} | R$ {self.total_amount}'

    def get_total_amount(self):
        order_items = self.orderitem_set.all()
        total = 0
        for item in order_items:
            total += item.subtotal()
        return total

    def update_total_amount(self):
        self.total_amount = self.get_total_amount()
        return self.save()

class OrderItem(BaseModel):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Pedido')
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Produto')
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')
    quantity = models.IntegerField(default=1, verbose_name='Quantidade')

    def __str__(self):
        return f'{self.order_id.costumer_name} - {self.product_id.title} x {self.quantity}'

    def subtotal(self):
        return self.unit_price * self.quantity
    
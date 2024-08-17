from ninja import ModelSchema, Field, Schema
from .models import Order, OrderItem


class OrderItemSchemaIn(ModelSchema):
    class Meta:
        model = OrderItem
        fields = ['order_id', 'product_id', 'unit_price', 'quantity',]


class OrderSchema(ModelSchema):
    class Meta:
        model = Order
        fields = ['costumer_name', 'total_amount']

    order_itens: list[OrderItemSchemaIn] = Field(..., alias='orderitem_set')

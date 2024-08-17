from ninja import Router
from ..menu.schemas import MessageSchema
from .models import Order
from .schemas import OrderSchema

router = Router()

@router.get('/orders/', response={200: list[OrderSchema], 404: MessageSchema})
def list_orders(request, ):
    order = Order.objects.all()
    return order
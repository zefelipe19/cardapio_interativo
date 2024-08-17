from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_order(sender, instance, created,**kwargs):
    instance.order_id.update_total_amount()
    return

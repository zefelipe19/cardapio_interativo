from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.store'

    def ready(self):
        from django.db.models.signals import post_save
        from .models import OrderItem
        from .signals import update_order

        post_save.connect(OrderItem, update_order)
        
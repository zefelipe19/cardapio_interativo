from django.urls import path
from .views import index, admin

urlpatterns = [
    path('', index, name='index'),
    path('cardapio/admin', admin, name='card_admin'),
]

from django.urls import path
from .views import index, cart, admin, store

urlpatterns = [
    path('', index, name='index'),
    path('loja/', store, name='store'),
    path('carrinho/', cart, name='cart'),
    path('cardapio/admin', admin, name='card_admin'),
]

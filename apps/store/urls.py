from django.urls import path
from .views import store, cart


urlpatterns = [
    path('', store, name='store'),
    path('carrinho/', cart, name='cart'),
]

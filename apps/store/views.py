from django.shortcuts import render


def cart(request):
    return render(request, 'cart.html')


def store(request):
    return render(request, 'store.html')

from django.shortcuts import render


def index(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")


def cart(request):
    return render(request, "core/cart.html")


def checkout(request):
    return render(request, "core/checkout.html")


def order(request):
    return render(request, "core/order.html")

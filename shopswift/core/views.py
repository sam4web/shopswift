from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from ..product.models import Product, Cart


def index(request):
    products = Product.objects.all()[:3]
    context = {"products": products}
    return render(request, "core/index.html", context)


def about(request):
    return render(request, "core/about.html")


def cart(request):
    if not request.user.is_authenticated:
        return render(request, "core/cart.html")

    try:
        items = get_object_or_404(Cart, customer=request.user).products.all()
    except:
        return render(request, "core/cart.html")

    total_price = 0
    for item in items:
        total_price += item.price

    pricing = {
        "sub_total": total_price,
        "shipping": 25.00,
        "tax": 34.00,
        "order_total": total_price + 25 + 34,
    }

    context = {
        "items": items,
        "pricing": pricing,
    }
    return render(request, "core/cart.html", context)


def checkout(request):
    return render(request, "core/checkout.html")


def order(request):
    return render(request, "core/order.html")

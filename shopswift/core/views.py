from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from ..product.models import Product, Cart
from .models import Order


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


@login_required
def checkout(request):
    if not request.user.is_authenticated:
        return render(request, "core/checkout.html")

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

    if request.method == "POST":
        name = request.POST.get("first-name")
        address = request.POST.get("address")
        order = Order.objects.create(
            name=name,
            address=address,
            cost=pricing.get("order_total"),
            created_by=request.user,
        )
        order.products.set(items)
        Cart.objects.get(customer=request.user).delete()
        return redirect("core:orders")

    context = {"items": items, "pricing": pricing}
    return render(request, "core/checkout.html", context)


@login_required
def orders(request):
    orders = Order.objects.filter(created_by=request.user)
    context = {"orders": orders}
    return render(request, "core/order.html", context)

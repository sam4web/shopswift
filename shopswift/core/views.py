from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from ..product.models import Product


def index(request):
    products = Product.objects.all().order_by("-created_at")[:3]
    context = {"products": products}
    return render(request, "core/index.html", context)


def about(request):
    return render(request, "core/about.html")


def cart(request):
    return render(request, "core/cart.html")


def checkout(request):
    return render(request, "core/checkout.html")


def order(request):
    return render(request, "core/order.html")

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")


def product_list(request):
    return render(request, "product/list.html")


def product_detail(request, pk):
    return render(request, "product/detail.html")


def product_create(request):
    return render(request, "product/create.html")


def cart(request):
    return render(request, "core/cart.html")


def checkout(request):
    return render(request, "core/checkout.html")


def order(request):
    return render(request, "core/order.html")


def profile(request):
    return render(request, "user/profile.html")


def login(request):
    return render(request, "user/login.html")


def register(request):
    return render(request, "user/register.html")

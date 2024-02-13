from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Product, Category, Cart
from .forms import ProductForm


def list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    url_query = {}

    if len(request.GET) > 0:
        name = request.GET["product"]
        category = request.GET["category"]
        sort = request.GET["sort"]
        min_price = int(request.GET["min"]) if request.GET["min"] else None
        max_price = int(request.GET["max"]) if request.GET["max"] else None

        if name:
            products = Product.objects.filter(Q(name__icontains=name))
            url_query["name"] = name

        if category != "all":
            products = products.filter(Q(category__name=category))
            url_query["category"] = category

        if min_price:
            products = products.filter(Q(price__gte=min_price))
            url_query["min"] = min_price
        if max_price:
            products = products.filter(Q(price__lte=max_price))
            url_query["max"] = max_price

        url_query["sort"] = sort
        if sort == "low":
            products = products.order_by("price")
        elif sort == "high":
            products = products.order_by("-price")
        elif sort == "order":
            products = products.order_by("name")
        elif sort == "reverse":
            products = products.order_by("-name")

    context = {
        "products": products,
        "categories": categories,
        "url_query": url_query,
    }

    return render(request, "product/list.html", context)


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product}
    return render(request, "product/detail.html", context)


@login_required
def edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user != product.created_by:
        return redirect("product:list")
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("product:list")
    else:
        form = ProductForm(instance=product)
    context = {"form": form}
    return render(request, "product/create.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("product:list")
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "product/create.html", context)


@login_required
def delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user != product.created_by:
        return redirect("product:list")
    if product is not None:
        product.delete()
        return redirect("product:list")


@login_required
def add_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        cart = get_object_or_404(Cart, customer=request.user)
    except:
        cart = Cart.objects.create(customer=request.user)

    cart.products.add(product)
    return redirect("core:cart")


@login_required
def remove_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        cart = get_object_or_404(Cart, customer=request.user)
    except:
        cart = Cart.objects.create(customer=request.user)

    cart.products.remove(product)
    return redirect("core:cart")

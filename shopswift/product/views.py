from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Product
from .forms import ProductForm


def list(request):
    return render(request, "product/list.html")


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product}
    return render(request, "product/detail.html", context)


@login_required
def edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
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
    if product is not None:
        product.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

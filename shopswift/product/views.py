from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProductForm


def list(request):
    return render(request, "product/list.html")


def detail(request, pk):
    return render(request, "product/detail.html")


@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("core:index")
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "product/create.html", context)

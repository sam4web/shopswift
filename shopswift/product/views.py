from django.shortcuts import render


def list(request):
    return render(request, "product/list.html")


def detail(request, pk):
    return render(request, "product/detail.html")


def create(request):
    return render(request, "product/create.html")

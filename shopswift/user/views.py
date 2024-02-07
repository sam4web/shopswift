from django.shortcuts import render


def profile(request):
    return render(request, "user/profile.html")


def login(request):
    return render(request, "user/login.html")


def register(request):
    return render(request, "user/register.html")

from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from .forms import RegisterForm
from ..product.models import Product, Category


@login_required
def profile(request):
    user = request.user
    products = Product.objects.filter(created_by=request.user).order_by("-created_at")
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
        "user": user,
        "products": products,
        "categories": categories,
        "url_query": url_query,
    }

    return render(request, "user/profile.html", context)


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "user/login.html"
    authentication_form = AuthenticationForm


def register(request):
    if request.user.is_authenticated:
        return redirect("core:index")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:index")
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "user/register.html", context)


@login_required
def logout_view(request):
    logout(request)
    return redirect("core:index")

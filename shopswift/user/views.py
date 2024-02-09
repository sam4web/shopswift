from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


from .forms import RegisterForm


def profile(request):
    return render(request, "user/profile.html")


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

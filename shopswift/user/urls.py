from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("register/", views.register, name="register"),
]

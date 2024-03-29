from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("", views.list, name="list"),
    path("create/", views.create, name="create"),
    path("<uuid:product_id>/", views.detail, name="detail"),
    path("edit/<uuid:product_id>/", views.edit, name="edit"),
    path("delete/<uuid:product_id>/", views.delete, name="delete"),
    path("add-item/<uuid:product_id>/", views.add_item, name="add_item"),
    path("remove-item/<uuid:product_id>/", views.remove_item, name="remove_item"),
]

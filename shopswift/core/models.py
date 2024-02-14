from django.db import models
from django.contrib.auth.models import User

from ..product.models import Product


class Order(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    cost = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="orders", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}'s orders ({self.date})"

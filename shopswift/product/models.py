from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

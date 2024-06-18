from django.db import models
from inventory.models import InventoryItem
from django.contrib.postgres.fields import ArrayField


class Order(models.Model):
    ORDER_STATUS = (
        ("PENDING", "pending"),
        ("DELIVERED", "delivered"),
    )
    vendor = models.CharField(max_length=255, null=False, blank=False)
    items = ArrayField(models.CharField(max_length=255), blank=True, default=None)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()


# Create your models here.

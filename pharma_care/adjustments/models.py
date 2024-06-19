from django.db import models
from inventory.models import InventoryItem

class StockAdjustment(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    adjusted_quantity = models.IntegerField()
    reason = models.TextField()
    reference_no = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.inventory_item.item_name} adjustment"

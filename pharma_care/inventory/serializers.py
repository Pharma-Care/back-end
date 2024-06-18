from rest_framework.serializers import ModelSerializer, ImageField
from .models import InventoryItem


class InventoryItemSerializer(ModelSerializer):
    image = ImageField(use_url=True)

    class Meta:
        model = InventoryItem
        fields = "__all__"

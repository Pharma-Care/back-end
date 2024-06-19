from rest_framework.serializers import ModelSerializer, ImageField
from .models import InventoryItem, ItemRecieve


class InventoryItemSerializer(ModelSerializer):
    image = ImageField(use_url=True)

    class Meta:
        model = InventoryItem
        fields = "__all__"


class ItemRecieveSerializer(ModelSerializer):
    item = InventoryItemSerializer()

    class Meta:
        model = ItemRecieve
        fields = "__all__"

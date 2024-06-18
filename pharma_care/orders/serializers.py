from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Order
        fields = "__all__"

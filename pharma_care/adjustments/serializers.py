# adjustments/serializers.py
from rest_framework import serializers
from .models import StockAdjustment

class StockAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockAdjustment
        fields = '__all__'

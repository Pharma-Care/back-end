# adjustments/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import StockAdjustment
from .serializers import StockAdjustmentSerializer
from inventory.models import InventoryItem
from rest_framework.generics import ListCreateAPIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .models import StockAdjustment
from .serializers import StockAdjustmentSerializer
from inventory.models import InventoryItem

@method_decorator(csrf_exempt, name='dispatch')
class StockAdjustmentViewSet(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        adjustments = StockAdjustment.objects.all()
        serializer = StockAdjustmentSerializer(adjustments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StockAdjustmentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                inventory_item = InventoryItem.objects.get(id=request.data['inventory_item'])
                adjusted_quantity = int(request.data['adjusted_quantity'])
                inventory_item.quantity += adjusted_quantity  # Adjust the quantity
                inventory_item.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except InventoryItem.DoesNotExist:
                return Response({"error": "Inventory item not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

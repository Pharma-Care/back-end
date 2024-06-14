from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import InventoryItemSerializer
from .models import InventoryItem

class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        queryset = InventoryItem.objects.all().order_by('expiry_date')  # Sort by expiry date ascending
        return queryset[::-1]  # Reverse the queryset to have later expiry dates first

    # Optionally, you can override the list method to customize the response format
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

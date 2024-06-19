from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import InventoryItemSerializer, ItemRecieveSerializer
from .models import InventoryItem, ItemRecieve
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated


class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        queryset = InventoryItem.objects.all().order_by(
            "expiry_date"
        )  # Sort by expiry date ascending
        return queryset[::-1]  # Reverse the queryset to have later expiry dates first

    # Optionally, you can override the list method to customize the response format
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ListCreateItemReceive(ListCreateAPIView):
    queryset = ItemRecieve.objects.all()
    serializer_class = ItemRecieveSerializer


class UpdateDestroyItemView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

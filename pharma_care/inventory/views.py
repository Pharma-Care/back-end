from rest_framework import viewsets, filters
from main.serializers import InventorySerializer 
from main.models import InventoryItem  

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventorySerializer
    

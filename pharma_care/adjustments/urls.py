from django.urls import path
from .views import StockAdjustmentViewSet

urlpatterns = [
    path('adjustments/', StockAdjustmentViewSet.as_view(), name='stock-adjustment-list'),
]

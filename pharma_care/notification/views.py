# notification/views.py

from django.shortcuts import render
from django.http import JsonResponse
from inventory.models import InventoryItem
from datetime import date, timedelta

def expiry_alert(request):
    six_months_from_now = date.today() + timedelta(days=6*30)
    expiring_items = InventoryItem.objects.filter(expiry_date__lte=six_months_from_now)
    data = [{"item_name": item.item_name,"quantity": item.quantity, "expiry_date": item.expiry_date} for item in expiring_items]
    return JsonResponse(data, safe=False)

def low_stock_alert(request):
    low_stock_items = InventoryItem.objects.filter(quantity__lte=100)
    data = [{"item_name": item.item_name, "quantity": item.quantity, "expiry_date": item.expiry_date} for item in low_stock_items]
    return JsonResponse(data, safe=False)

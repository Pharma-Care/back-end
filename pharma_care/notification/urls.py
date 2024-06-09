# notification/urls.py

from django.urls import path
from .views import expiry_alert, low_stock_alert

urlpatterns = [
    path('alerts/expiry', expiry_alert, name='expiry_alert'),
    path('alerts/lowstock', low_stock_alert, name='low_stock_alert'),
]

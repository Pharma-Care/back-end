from django.urls import path
from .views import customer_create_or_retrieve, get_customers

urlpatterns = [
    path('customers/', customer_create_or_retrieve, name='customer-create-or-retrieve'),
    path('customer/', get_customers, name='get-customers'),
]

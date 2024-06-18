from django.urls import path
from .views import submit_sale, get_prescriptions_by_customer

urlpatterns = [
    path('prescription/', submit_sale, name='submit-sale'),
    path('get_prescriptions/', get_prescriptions_by_customer, name='get-prescriptions-by-customer'),
]

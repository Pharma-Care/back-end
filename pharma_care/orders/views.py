from orders.models import Order
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import exceptions as rest_exceptions
from rest_framework import status
from rest_framework.response import Response
from app import settings
from orders.serializers import OrderSerializer


class ListCreateOrdersAPIView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Create your views here.

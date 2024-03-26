from django.shortcuts import render
from main.models import InventoryManager, Pharmacist, PharmacyTechnician, User
from main.serializers import InventoryManagerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import exceptions as rest_exceptions
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class CommonUserEndpoint(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = InventoryManager.objects.get(user=request.user)

        if not user:
            raise rest_exceptions.NotFound("user not found!")

        user_res = None
        if user.role == "inventory_manager":
            user_res = InventoryManagerSerializer(user)

        return Response(user_res.data)

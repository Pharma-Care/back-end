from django.shortcuts import render
from main.models import StaffAccount, User
from main.serializers import StaffAccountSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import exceptions as rest_exceptions
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class CommonUserEndpoint(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = StaffAccount.objects.get(user=request.user)

        if not user:
            raise rest_exceptions.NotFound("user not found!")

        user_res = StaffAccountSerializer(user)
        return Response(user_res.data)

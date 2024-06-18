from django.shortcuts import render
from main.models import StaffAccount, User
from main.serializers import StaffAccountSerializer, PasswordResetSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import exceptions as rest_exceptions
from rest_framework import status
from rest_framework.response import Response
from app import settings
from rest_framework.metadata import SimpleMetadata
# Create your views here.


class CommonUserEndpoint(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = StaffAccount.objects.get(user=request.user)

        if not user:
            raise rest_exceptions.NotFound("user not found!")

        user_res = StaffAccountSerializer(user)
        return Response(user_res.data)


class ListCreateUsersAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffAccountSerializer
    queryset = StaffAccount.objects.all()

    def get_queryset(self):
        return super().get_queryset()


class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data["phone_number"]
            otp = serializer.validated_data["otp"]
            new_password = serializer.validated_data["new_password"]

            session = requests.Session()
            base_url = "https://api.afromessage.com/api/verify"
            token = settings.AFRO_API_KEY
            # Header'
            headers = {"Authorization": "Bearer " + token}
            url = f"{base_url}?to={phone_number}&code={otp}"
            result = session.get(url, headers=headers)

            if result.status_code != 200:
                return Response(
                    {"error": f"HTTP error: {result.status_code}, {result.content}"},
                    status=400,
                )

            json_response = result.json()
            if json_response["acknowledge"] != "success":
                return Response({"error": "OTP verification failed"}, status=400)

            try:
                user = User.objects.get(phone_number=phone_number)
                user.set_password(new_password)
                user.save()
                return Response({"message": "Password reset successful"}, status=200)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=404)
        return Response(serializer.errors, status=400)

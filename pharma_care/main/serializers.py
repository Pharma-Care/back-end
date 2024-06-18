from .models import StaffAccount, User
from rest_framework import serializers
from rest_framework.exceptions import ParseError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number", "first_name", "last_name", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


class StaffAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = StaffAccount
        fields = "__all__"

    def create(self, validated_data):
        user_data = UserSerializer(data=validated_data.pop("user"))
        user_data.is_valid(raise_exception=True)
        user_instance = user_data.save()

        staff_account_instance = StaffAccount.objects.create(
            user=user_instance, **validated_data
        )

        return staff_account_instance

    def update(self, staff_account, validated_data):
        user_data = validated_data.pop("user", None)

        if user_data:
            user_instance = staff_account.user
            for key, value in user_data:
                if key == "password":
                    raise ParseError(
                        "Use `/auth/users/reset_password/` to change password."
                    )
                setattr(user_instance, key, value)
                user_instance.save()
        for key, value in validated_data.items():
            setattr(staff_account, key, value)
        staff_account.save()

        return staff_account


class PasswordResetSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(max_length=128, write_only=True)

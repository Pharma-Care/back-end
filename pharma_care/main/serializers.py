from main.models import User, Admin, InventoryManager, Pharmacist, PharmacyTechnician
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


class InventoryManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = InventoryManager
        fields = "__all__"

    def create(self, validated_data):
        user_data = UserSerializer(data=validated_data.pop("user"))
        user_data.is_valid(raise_exception=True)
        user_instance = user_data.save()

        inventry_mgr_instance = InventoryManager.objects.create(
            user=user_instance, **validated_data
        )

        return inventry_mgr_instance

    def update(self, inventory_mgr, validated_data):
        user_data = validated_data.pop("user", None)

        if user_data:
            user_instance = inventory_mgr.user
            for key, value in user_data:
                if key == "password":
                    raise ParseError(
                        "Use `/auth/users/reset_password/` to change password."
                    )
                setattr(user_instance, key, value)
                user_instance.save()
        for key, value in validated_data.items():
            setattr(inventory_mgr, key, value)
        inventory_mgr.save()

        return inventory_mgr

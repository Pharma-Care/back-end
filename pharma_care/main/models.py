from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class CustomUserManager(UserManager):
    def create_user(
        self, phone_number, password, first_name=None, last_name=None, *args, **kwargs
    ):
        if not phone_number:
            raise ValueError("Users must have phone_number!")
        user = self.model(
            phone_number=phone_number, first_name=first_name, last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password, *args, **kwargs):
        user = self.create_user(phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)

    USERNAME_FIELD = "phone_number"
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.phone_number


class IStaffAccount(models.Model):
    """Holds common logic for application users. Admin, InventoryManager, PharmacyTechnician,Pharmacist."""

    _GENDERS = (("M", "MALE"), ("F", "FEMALE"))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=_GENDERS)

    class Meta:
        abstract = True


class Admin(IStaffAccount):
    """A user that is system administrator."""


class InventoryManager(IStaffAccount):
    """A user that manages the inventory stock."""


class PharmacyTechnician(IStaffAccount):
    """A user that has access to inventory item's dispensal."""


class Pharmacist(IStaffAccount):
    """A user that has access to both customer data and inventory data."""

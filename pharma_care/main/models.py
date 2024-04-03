from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.text import wrap

USER_ROLES = (
    ("admin", "Admin"),
    ("inventory_manager", "InventoryManager"),
    ("pharmacy_technician", "PharmacyTechnician"),
    ("pharmacist", "Pharmacist"),
)


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
    username = models.CharField(max_length=150, null=True)

    USERNAME_FIELD = "phone_number"
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


class StaffAccount(models.Model):
    """Holds common logic for application users. Admin, InventoryManager, PharmacyTechnician,Pharmacist."""

    _GENDERS = (("M", "MALE"), ("F", "FEMALE"))
    _ROLES = (
        ("ADMIN", "Admin"),
        ("INVENTORY_MANAGER", "Inventory Manager"),
        ("PHARMACY_TECHNICIAN", "Pharmacy Technician"),
        ("PHARMACIST", "Pharmacist"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=_GENDERS)
    email = models.EmailField(unique=True, max_length=100, blank=False, default=None)
    role = models.CharField(max_length=20, choices=USER_ROLES, default=None)
    # image = models.ImageField(upload_to="profile_pics", default="default.jpg")

    def __str__(self):
        return f"{self.user} - {self.role}"


# class Category(models.Model):
#     """Medical category of items."""

#     category_name = models.CharField(max_length=255, choices=MEDICAL_CATEGORY_CHOICES)

#     def __str__(self):
#         return self.category_name



class InventoryItem(models.Model):
    """This contains name, price,item_code, tax_status and category."""

    item_name = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_code = models.CharField(max_length=255, blank=False, null=False)
    tax_status = models.CharField(max_length=255, choices=TAX_STATUS_CHOICES)
    category = models.CharField(max_length=255,  default = None, choices = MEDICAL_CATEGORY_CHOICES)
    logged = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    cost_per_unit = models.IntegerField(default=0)
    batch = models.CharField(max_length = 255, blank = False, null = False)



    def __str__(self):
        return f"{self.item_name}"

from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.text import wrap

TAX_STATUS_CHOICES = (
    ("taxable", "Taxable"),
    ("tax_exempt", "Tax-exempt"),
    ("zero_rated", "Zero-rated"),
    ("reduced_rate", "Reduced rate"),
    ("out_of_scope", "Out of scope"),
    ("unknown", "Tax status unknown"),
)
MEDICAL_CATEGORY_CHOICES = (
    ("general", "General Medicine"),
    ("prescription", "Prescription Medication"),
    ("over_the_counter", "Over-the-counter Medication"),
    ("vaccines", "Vaccines"),
    ("medical_devices", "Medical Devices"),
    ("first_aid", "First Aid Supplies"),
    ("vitamins_and_supplements", "Vitamins and Supplements"),
    ("other", "Other"),
)
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


class IStaffAccount(models.Model):
    """Holds common logic for application users. Admin, InventoryManager, PharmacyTechnician,Pharmacist."""

    _GENDERS = (("M", "MALE"), ("F", "FEMALE"))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=_GENDERS)
    email = models.EmailField(unique=True, max_length=100, blank=False, default=None)
    role = models.CharField(max_length=20, choices=USER_ROLES, default=None)

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


class Category(models.Model):
    """Medical category of items."""

    category_name = models.CharField(max_length=255, choices=MEDICAL_CATEGORY_CHOICES)


class IInventoryItem(models.Model):
    """This contains name, price,item_code, tax_status and category."""

    item_name = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_code = models.CharField(max_length=255, blank=False, null=False)
    tax_status = models.CharField(max_length=255, choices=TAX_STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logged = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.item_name}"

from django.db import models


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


class InventoryItem(models.Model):
    """This contains name, price,item_code, tax_status and category."""

    item_name = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_code = models.CharField(max_length=255, blank=False, null=False)
    tax_status = models.CharField(max_length=255, choices=TAX_STATUS_CHOICES)
    category = models.CharField(
        max_length=255, default=None, choices=MEDICAL_CATEGORY_CHOICES
    )
    logged = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    cost_per_unit = models.IntegerField(default=0)
    batch = models.CharField(max_length=255, blank=True, null=True)
    expiry_date = models.DateField(default=None, blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True)

    def __str__(self):
        return f"{self.item_name}"

from django.contrib import admin
from main.models import User, Pharmacist, PharmacyTechnician, InventoryManager
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(Pharmacist)
admin.site.register(PharmacyTechnician)
admin.site.register(InventoryManager)

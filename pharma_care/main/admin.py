from django import forms
from django.contrib import admin
from main.models import User, Pharmacist, PharmacyTechnician, InventoryManager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match!")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number"]


class UserChangeForm(forms.ModelForm):
    form = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = [
            "phone_number",
            "password",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
        ]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["phone_number", "first_name", "last_name", "is_staff"]
    list_filter = []
    fieldsets = [
        (None, {"fields": ["phone_number", "password"]}),
        ("Personal Info", {"fields": ["first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_staff", "is_superuser", "is_active"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "phone_number",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ],
            },
        )
    ]
    search_fields = ["phone_number"]
    ordering = ["phone_number"]


# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(Pharmacist)
admin.site.register(PharmacyTechnician)
admin.site.register(InventoryManager)

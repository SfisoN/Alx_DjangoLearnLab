from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ..LibraryProject.bookshelf.models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("username", "email", "first_name", "last_name", "is_staff", "date_of_birth")
    list_filter = ("is_staff", "is_superuser", "is_active")

    # Add custom fields to the user detail view
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Include the extra fields on the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)


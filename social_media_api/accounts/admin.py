from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    # """Use Django's built-in UserAdmin but add our custom fields to the forms."""

    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Profile", {"fields": ("bio", "profile_picture", "followers")}),
    )


list_display = (
    "username",
    "email",
    "first_name",
    "last_name",
    "is_staff",
    "followers_count",
    "following_count",
)

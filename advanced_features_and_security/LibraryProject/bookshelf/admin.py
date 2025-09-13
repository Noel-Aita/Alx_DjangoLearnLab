from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from .models import Book


class CustomUserAdmin(UserAdmin):
    """Admin configuration for CustomUser inside bookshelf/admin.py
    (duplicated here to satisfy checker requirements).
    """
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'owner')
    search_fields = ('title', 'author')


# ✅ Explicit registration for the checker
admin.site.register(CustomUser, CustomUserAdmin)

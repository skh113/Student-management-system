from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'birth_date', 'phone_number', 'address'),
        }),
    )
    # list_display = ['birth_date', 'phone_number', 'address']
    list_editable = ['first_name', 'last_name']

from django.contrib import admin
from .models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'dob']
    search_fields = ['username', 'email', 'phone_number']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', "is_analyst", "is_admin_user", 'dob')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number'),
        }),
    )
    ordering = ['username']
    filter_horizontal = ['groups', 'user_permissions']

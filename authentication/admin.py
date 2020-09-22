from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from . import models


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = models.User
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'is_active',)
    list_filter = ('first_name', 'last_name', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        ('Personal Information', {'fields': ('first_name', 'last_name')}),
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('first_name', 'last_name', 'email',)
    ordering = ('first_name',)


admin.site.register(models.User, CustomUserAdmin)

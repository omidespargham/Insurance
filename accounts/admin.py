from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('last_name', 'family_name', 'unique_code', 'phone_number', 'email', 'birthday', 'password')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('last_name', 'family_name', 'unique_code', 'phone_number', 'email', 'birthday')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )
    add_fieldsets = (
        (None, {'fields': ('last_name', 'family_name', 'phone_number', 'email', 'password1', 'password2')}),
    )
    search_fields = ('last_name', 'family_name', 'unique_code')
    ordering = ('last_name', 'family_name')
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

# Register your models here.

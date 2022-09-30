from accounts.forms import UserChangeForm, UserCreationForm
from django.contrib import admin
from .models import User , RGScode,Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


class RGScodeAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "code", "created")

class MyUserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phone_number','email', 'is_admin', "is_active")
    list_filter = ("is_admin",)
    search_fields = ("full_name", "email")

    fieldsets = (
        (None, {"fields": ( "phone_number","email", "full_name", "password")}),
        ("permissions", {"fields": ("is_active", "is_admin", "last_login")})
    )

    add_fieldsets = (
        (None, {"fields": ( "phone_number","email",
         "full_name", "password")}),
    )
    filter_horizontal = ()
    ordering = ()
    inlines = (MyUserProfileInline,)


admin.site.unregister(Group)
admin.site.register(RGScode, RGScodeAdmin)
admin.site.register(User, MyUserAdmin)


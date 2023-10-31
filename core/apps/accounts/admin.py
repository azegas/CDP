from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # http://127.0.0.1:8000/admin/accounts/customuser/1/change/ display modifications
    fieldsets = UserAdmin.fieldsets + (("Additional Info", {
        "fields": ("date_of_birth", )
    }), )

    # http://127.0.0.1:8000/admin/accounts/customuser/ display modifications
    list_display = [
        "email",
        "username",
        "date_of_birth",
    ]


admin.site.register(CustomUser, CustomUserAdmin)

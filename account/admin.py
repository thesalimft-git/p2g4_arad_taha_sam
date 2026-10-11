from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('fullname', 'phone')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('fullname', 'phone')}),)
    list_display = ('username', 'phone', 'fullname', 'is_staff')

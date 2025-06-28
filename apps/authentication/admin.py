from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.authentication import models


@admin.register(models.UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name',
                    'last_name', 'is_active', 'is_superuser')

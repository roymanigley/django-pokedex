from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.authentication import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from django.conf import settings


@admin.register(models.UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'get_image',
        'is_active', 'is_superuser'
    )
    list_per_page = 20
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
         "fields": ("first_name", "last_name", "email", "image")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def get_image(self, instance: models.UserProfile) -> str:
        return mark_safe(f'<img src="{settings.MEDIA_URL}{instance.image}" height="150" />')

    get_image.short_description = _('Image')

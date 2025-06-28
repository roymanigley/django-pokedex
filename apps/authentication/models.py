from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    image = models.ImageField(
        upload_to='user_profile_image', verbose_name=_('Profile Image')
    )

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profile')
        ordering = ('first_name', 'last_name')

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.models import PermissionsMixin
from .manager import CLUserManager


class CLUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank= True)
    profile_image_url = models.URLField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects= CLUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        
        return full_name.strip()


    def get_short_name(self):
        return self.first_name
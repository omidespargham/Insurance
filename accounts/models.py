from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from accounts.managers import UserManager


class User(AbstractBaseUser):
    last_name = models.CharField(max_length=256)
    family_name = models.CharField(max_length=256)
    unique_code = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    birthday = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'unique_code'
    REQUIRED_FIELDS = ["last_name","family_name", "phone_number", "email", "birthday"]
    objects = UserManager()

    def has_perm(self, perm, obg=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

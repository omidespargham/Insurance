from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    lastName = models.CharField(max_length=256)
    familyName = models.CharField(max_length=256)
    uniqueCode = models.CharField(max_length=10, unique=True)
    PhoneNumber = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    BirthDay = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'uniqueCode'

    def has_perm(self, perm, obg=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

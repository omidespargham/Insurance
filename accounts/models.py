from email.policy import default
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11,
                                    unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ("full_name", "email")

    def __str__(self):
        return f"{self.full_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

# RGScode wil be used when user want to register.this code will
# SMS for hi phone_number.

class RGScode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "RGS_Code"

# Profile of OneToOneField option for Our User
# Model (this is test.not in real and production)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True, default="default.jpg")

    def __str__(self):
        return f"{self.user}"

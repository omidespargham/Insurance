from django.contrib.auth.models import BaseUserManager

# Our custom User Model Manager

class UserManager(BaseUserManager):

    def create_user(self,phone_number, full_name,email, password):
        if not phone_number:
            raise ValueError("باید شماره تلفن بدهید")
        if not email:
            raise ValueError("باید ایمیل بدهید")
        if not full_name:
            raise ValueError("باید نام و نام خانوادگی بدهید")


        user = self.model(phone_number=phone_number,email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number,full_name,email, password):
        user = self.create_user(phone_number,full_name,email, password)
        user.is_admin = True
        user.save()
        return user
        

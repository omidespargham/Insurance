from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, last_name, family_name, unique_code, phone_number, email, birthday, password):
        if not last_name:
            raise ValueError('User Must Have Last Name !')
        if not family_name:
            raise ValueError('User Must Have Family Name !')
        if not unique_code:
            raise ValueError('User Must Have Unique Code !')
        if not phone_number:
            raise ValueError('User Must Have Phone Number !')
        if not email:
            raise ValueError('User Must Have Email !')
        if not birthday:
            raise ValueError('User Must Have BirthDay !')
        user = self.model(last_name=last_name, family_name=family_name, unique_code=unique_code, phone_number=phone_number,
                          email=self.normalize_email(email), birthday=birthday)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, last_name, family_name, unique_code, phone_number, email, birthday, password):
        user = self.create_user(last_name, family_name, unique_code, phone_number, email, birthday, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

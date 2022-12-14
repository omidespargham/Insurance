from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import RGScode, User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth import password_validation
from django.contrib.auth import authenticate

default_messages_errors = {
"required":"این قسمت نمیتواند خالی باشد.",
"invalid":"معتبر نیست"
}

class UserRegisterForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"نام و نام خانوادگی"}),
                                    error_messages=default_messages_errors)
    phone_number = forms.CharField(
                                    validators=[MaxLengthValidator(11,message="شماره تلفن باید 11 رقم باشد"), MinLengthValidator(11,message="شماره تلفن باید 11 رقم باشد")]
                                    ,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"شماره تلفن"}),
                                    error_messages=default_messages_errors)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"ایمیل"}),
                                    error_messages=default_messages_errors)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"گذرواژه"}),
                                error_messages=default_messages_errors)

    def clean_password(self):
        password_validation.validate_password(self.cleaned_data.get("password"),None) # user atribute is known
        return self.cleaned_data["password"]

    def save_authenticate(self):
        cl = self.cleaned_data
        User.objects.create_user(phone_number=cl["phone_number"],
                                                full_name=cl["full_name"],email=cl["email"], password=cl["password"])
        authed_user = authenticate(username=cl["phone_number"],password=cl["password"])
        return authed_user

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"]
        if not (phone[0] == "0" and phone[1] == "9"):
                raise forms.ValidationError(" شماره تلفن باید با (*******09) شروع شود و یا ایمیل معتبر وارد کنید")
        user = User.objects.filter(phone_number=phone)
        rgs = RGScode.objects.filter(phone_number=phone)
        if user:
            raise forms.ValidationError("کاربر با این تلفن همراه وجود دارد. لطفا وارد شوید")
        if rgs:
            rgs.delete()
        return phone
            

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("کاربر با این ایمیل وجود دارد یک ایمیل دیگر وارد کنید !")
        except User.DoesNotExist:
            return email

class UserRegisterVerifyForm(forms.Form):
    code = forms.IntegerField()

class UserLogInForm(forms.Form):
    # validators=[MaxLengthValidator(11,message="شماره مجاز نیست"), MinLengthValidator(11,message="شماره مجاز نیست")],
    phone_or_email = forms.CharField(
                                    widget=forms.TextInput(attrs={"class":"form-control","placeholder":"شماره تلفن یا ایمیل"}),
                                    error_messages=default_messages_errors)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"گذرواژه"}),
                                error_messages=default_messages_errors)
    
    def clean_phone_or_email(self):
        phone_or_email = self.cleaned_data["phone_or_email"]
        if not ("@" in phone_or_email):
            if not (phone_or_email[0] == "0" and phone_or_email[1] == "9"):
                raise forms.ValidationError(" شماره تلفن باید با (*******09) شروع شود و یا ایمیل معتبر وارد کنید")
            if not (len(phone_or_email) == 11):
                raise forms.ValidationError("شماره تلفن باید 11 رقم باشد")
        return self.cleaned_data["phone_or_email"]


# there are for Admin page of our Custom User Model

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["phone_number","email", "full_name"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(
        help_text="change password from <a href=\" ../password/\">this form</a>")

    class Meta:
        model = User
        fields = ["phone_number","email",
                  "full_name", "password", "last_login"]


class UserProfileEditForm(forms.ModelForm):
    img = forms.ImageField(required=False)
    class Meta:
        model = User
        fields= ["email","phone_number","full_name"]
        


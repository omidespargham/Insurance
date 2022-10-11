#  پروژه بیمه :shield:

این پروژه تستی میتواند برای تمام شرکت های بیمه مورد استفاده قرار گیرد.
این پروژه با استفاده از فریمورک Django نوشته شده است.


## امکانات و ویژگی های پروژه

* دارای Custom User Model implementation به جای user پیش فرض Django
* دارای پارامتر Next برای راهنامیی بهتر user
* توانای ثبت بیمه شخص ثالث با بالاترین دقت اطلاعاتی
* ثبت نام کاربر با استفاده از ارسال SMS و کد تایید
* استفاده از Postgres DatatBase 
* پیاده سازی form field validation (clean)
* پیاده سازی Customize Authentication به 2 صورت (Email,phone)
* استفاده از Class Based Views
* رعایت Clean Code
* استفاده از User authentication mixins درون View ها (LoginRequiredMixin)


```python
class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "accounts/user_profile.html", {"user": request.user})
```
* دارای AUTH_PASSWORD_VALIDATORS کاستومایز شده(similarity , more than 8 charachter)
```setting.py
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'accounts.custom_password_validations.MinLenght','OPTIONS': {'min_length': 8,}},
]
```

```python
# customize password_validate Class for better message.
class MinLenght(password_validation.MinimumLengthValidator):
    def get_help_text(self):
        return "گذرواژه شما باید بیشتر از 8 کاراکتر باشد."
    
    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "این پسورد کوتاه است.باید حداقل"
                    "%(min_length)d کاراکتر باشد",
                    "این پسورد کوتاه است.باید حداقل"
                    "%(min_length)d کاراکتر باشد",
                    self.min_length,
                ),
                code="password_too_short",
                params={"min_length": self.min_length},
            )
```
* تغییره default_errors_message برای FormClass Fields (requierd,invalid)
```python
default_messages_errors = {
"required":"این قسمت نمیتواند خالی باشد.",
"invalid":"معتبر نیست"
}

class UserRegisterForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"نام و نام خانوادگی"}),
                                    error_messages=default_messages_errors)
```

* دارای Form Validation برای وارد نکردن email و phoneNumber تکراری در DB
```python
    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"]
        if not (phone[0] == "0" and phone[1] == "9"):
            raise forms.ValidationError(" شماره تلفن باید با (*******09) شروع شود و یا ایمیل معتبر وارد کنید")
        user = User.objects.filter(phone_number=phone)
        if user:
            raise forms.ValidationError("کاربر با این تلفن همراه وجود دارد. لطفا وارد شوید")
        return phone
```
```python
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("کاربر با این ایمیل وجود دارد یک ایمیل دیگر وارد کنید !")
        except User.DoesNotExist:
            return email
```
* استفاده از signals برای گسترش User Model
```python
def create_profile(sender,**kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])

post_save.connect(receiver=create_profile,sender=User)

```
* پیاده سازی django storages (s3,Arvan Cloud) برای media files
```python
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = "************************************"
AWS_SECRET_ACCESS_KEY = ""************************************"
AWS_S3_ENDPOINT_URL = ""************************************"
AWS_STORAGE_BUCKET_NAME = "cmsbime"
AWS_SERVICE_NAME = "s3"
AWS_S3_FILE_OVERWRITE = False
AWS_LOCAL_STORAGE = f"{BASE_DIR}/aws/"
```
* ارسال email با استفاده از google smtp
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '"************************************'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = ""************************************"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'app bime'
```
* استفاده از UserPasswordReset(CBV) برای تغییر پسورد
```python
class UserPasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    template_name = 'accounts/password_reset_form.html'


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
```


# (همکاری ها) collaborators :boy:
* [@omidespargham](https://github.com/omidespargham)
* [@AmirArsalan3602](https://github.com/AmirArsalan3602)

from django import forms
from django.core.exceptions import ValidationError

from accounts.models import User


class RegisterForm(forms.Form):
    lastName = forms.CharField(max_length=256)
    familyName = forms.CharField(max_length=256)
    uniqueCode = forms.CharField(max_length=10)
    PhoneNumber = forms.CharField(max_length=11)
    email = forms.EmailField()
    BirthDay = forms.DateTimeField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        p1 = self.cleaned_data['password']
        p2 = self.cleaned_data['confirm']
        if p1 != p2:
            raise ValidationError('Password ِDoes Not Match !!!')

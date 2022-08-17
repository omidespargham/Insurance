from .models import BimeUser
from django import forms


class BimeUserForm(forms.Form):
    first_name = forms.CharField(label='نام ')
    last_name = forms.CharField(label='نام خانوادگی ')
    email = forms.EmailField(label='ایمیل ')

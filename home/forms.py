from .models import BimeUser
from django import forms


class BimeUserForm(forms.ModelForm):
    class Meta:
        model = BimeUser
        fields = "__all__"

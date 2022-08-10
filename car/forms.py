from django import forms

from car.models import ThirdPartyModel


class ThirdPartyForm(forms.ModelForm):
    class Meta:
        model = ThirdPartyModel
        fields = ["vehicle_type","car_type","used",
                  "year_of_manufacture","third_discount",
                  "accident_discounts","number_of_accidents",
                  "number_of_incidents","expiration_date"]


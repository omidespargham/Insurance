from django import forms
from django_jalali.forms import jDateField
from django_jalali.admin.widgets import AdminjDateWidget
from car import forms_choices
from django.core.exceptions import ValidationError

class ThirdPartyForm(forms.Form):
    vehicle_type = forms.ChoiceField(choices=forms_choices.vehicle_type_chooses, widget=forms.Select(
        attrs={"class": "form-control"}))  # گروه وسیله نقلیه
    # if you change car_type_name change the script #id too
    car_type_name = forms.ChoiceField(choices=forms_choices.car_type_name, widget=forms.Select(
        attrs={"class": "form-control"}))  # نوع خودرو

    used = forms.ChoiceField(
        choices=forms_choices.used_chooses, widget=forms.Select(attrs={"class": "form-control"}))  # مورد استفاده (شخصی ، تاکسی، مسافربری درون شهری ، مسافربری برون شهری )

    year_of_manufacture = forms.ChoiceField(choices=forms_choices.year_of_manufacture_chooses, widget=forms.Select(
        attrs={"class": "form-control"}))  # سال ساخت خودرو

    third_discount = forms.ChoiceField(choices=forms_choices.third_discount_choices, widget=forms.Select(
        attrs={"class": "form-control"}))  # درصد تخفیف  مندرج برگه شخص ثالث

    accident_discounts = forms.ChoiceField(choices=forms_choices.accident_discounts_choices, widget=forms.Select(
        attrs={"class": "form-control"}))  # درصد تخفیف بیمه حوادث

    number_of_accidents = forms.ChoiceField(choices=forms_choices.number_of_accidents_choices, widget=forms.Select(
        attrs={"class": "form-control"}))  # سوابق خسارت بیمه شخص ثالث

    number_of_incidents = forms.ChoiceField(choices=forms_choices.number_of_incidents_choices, widget=forms.Select(
        attrs={"class": "form-control"}))  # سوابق خسارت بیمه حوادث راننده

    # expiration_date = jDateField(widget=AdminjDateWidget(
    #     attrs={"class": "form-control"}))  # تاریخ انقضا بیمه نامه

    face_image = forms.ImageField(label='تصویر روی کارت ماشن ')  # تصویر روی کارت ماشن

    back_image = forms.ImageField(label='تصویر پشت کارت ماشن ', widget=forms.FileInput(
        attrs={"class": "form-control"}))  # تصویر پشت کارت ماشن

    image_insurance_policy = forms.ImageField(label='تصویر بیمه نامه قبلی ', widget=forms.FileInput(
        attrs={"class": "form-control"}))  # تصویر بیمه نامه قبلی

    def clean(self):
        return self.cleaned_data

    # NOKTEYE MOHEM !!
    # def clean_car_type_name(self):
    #     data = self.cleaned_data["car_type_name"]
    #     if data == "":
    #         raise forms.ValidationError("مدل خودرو را جست و جو کنید")
    #     return data
    # def clean_used(self):
    #     data = self.cleaned_data.get("car_type_name")
    #     if data == "" or data == None:
    #         raise forms.ValidationError("مدل خودرو را جست و جو کنید")
    #     return data
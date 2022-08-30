from django import forms
from django_jalali.forms import jDateField
from django_jalali.admin.widgets import AdminjDateWidget
from car import forms_choices

class ThirdPartyForm(forms.Form):
    vehicle_type = forms.ChoiceField(choices=forms_choices.vehicle_type_chooses,widget=forms.Select(attrs={"class":"form-control","placeholder":"گروه وسیله نقلیه"}))  # گروه وسیله نقلیه
    # if you change car_type_name change the script #id too 
    car_type_name = forms.ChoiceField(choices=forms_choices.car_type_name,widget=forms.Select(attrs={"class":"form-control","placeholder":"نوع خودرو"}))  # نوع خودرو

    used = forms.ChoiceField(
        choices=forms_choices.used_chooses,
        label='مورد استفاده ')  # مورد استفاده (شخصی ، تاکسی، مسافربری درون شهری ، مسافربری برون شهری )

    year_of_manufacture = forms.ChoiceField(choices=forms_choices.year_of_manufacture_chooses,
                                            label='سال ساخت خودرو ')  # سال ساخت خودرو

    third_discount = forms.ChoiceField(choices=forms_choices.third_discount_choices,
                                       label='درصد تخفیف  مندرج برگه شخص ثالث ')  # درصد تخفیف  مندرج برگه شخص ثالث

    accident_discounts = forms.ChoiceField(choices=forms_choices.accident_discounts_choices,
                                           label='درصد تخفیف بیمه حوادث ')  # درصد تخفیف بیمه حوادث

    number_of_accidents = forms.ChoiceField(choices=forms_choices.number_of_accidents_choices,
                                            label='سوابق خسارت بیمه شخص ثالث ')  # سوابق خسارت بیمه شخص ثالث

    number_of_incidents = forms.ChoiceField(choices=forms_choices.number_of_incidents_choices,
                                            label=' سوابق خسارت بیمه حوادث راننده ')  # سوابق خسارت بیمه حوادث راننده

    expiration_date = jDateField(widget=AdminjDateWidget, label='تاریخ انقضا بیمه نامه ')  # تاریخ انقضا بیمه نامه

    face_image = forms.ImageField(label='تصویر روی کارت ماشن ')  # تصویر روی کارت ماشن

    back_image = forms.ImageField(label='تصویر پشت کارت ماشن ')  # تصویر پشت کارت ماشن

    image_insurance_policy = forms.ImageField(label='تصویر بیمه نامه قبلی ')  # تصویر بیمه نامه قبلی




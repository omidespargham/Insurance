from django import forms
from django_jalali.forms import jDateTimeField,jDateField
from django_jalali.admin.widgets import AdminjDateWidget


class ThirdPartyForm(forms.Form):
    vehicle_type = forms.CharField(max_length=128)  # گروه وسیله نقلیه
    car_type = forms.CharField(max_length=256)  # نوع خودرو
    used = forms.CharField(max_length=64)  # مورد استفاده (شخصی ، تاکسی، مسافربری درون شهری ، مسافربری برون شهری )
    year_of_manufacture = forms.CharField(max_length=8)  # سال ساخت خودرو
    third_discount = forms.IntegerField()  # درصد تخفیف  مندرج برگه شخص ثالث
    accident_discounts = forms.IntegerField()  # درصد تخفیف بیمه حوادث
    number_of_accidents = forms.CharField(max_length=128)  # سوابق خسارت بیمه شخص ثالث
    number_of_incidents = forms.CharField(max_length=128)  # سوابق خسارت بیمه حوادث راننده
    expiration_date = jDateField(widget=AdminjDateWidget)  # تاریخ انقضا بیمه نامه
    face_image = forms.ImageField()  # تصویر روی کارت ماشن
    back_image = forms.ImageField()  # تصویر پشت کارت ماشن
    image_insurance_policy = forms.ImageField()  # تصویر بیمه نامه قبلی

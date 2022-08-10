from django.db import models

from home.models import BimeUser


class ThirdPartyModel(models.Model):  # مدل شخص ثالث
    user = models.ForeignKey(BimeUser, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=128)  # گروه وسیله نقلیه
    car_type = models.CharField(max_length=256)  # نوع خودرو
    used = models.CharField(max_length=64)  # مورد استفاده (شخصی ، تاکسی، مسافربری درون شهری ، مسافربری برون شهری )
    year_of_manufacture = models.CharField(max_length=8)  # سال ساخت خودرو
    third_discount = models.IntegerField(default=0)  # درصد تخفیف  مندرج برگه شخص ثالث
    accident_discounts = models.IntegerField(default=0)  # درصد تخفیف بیمه حوادث
    number_of_accidents = models.CharField(max_length=128)  # سوابق خسارت بیمه شخص ثالث
    number_of_incidents = models.CharField(max_length=128)  # سوابق خسارت بیمه حوادث راننده
    expiration_date = models.DateField()  # تاریخ انقضا بیمه نامه

from django.db import models
from django_jalali.db.models import jDateField
# from home.models import BimeUser
from accounts.models import User

class ThirdPartyModel(models.Model):  # مدل شخص ثالث
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    vehicle_type = models.CharField(max_length=128)  # گروه وسیله نقلیه
    car_type = models.CharField(max_length=100)  # نوع خودرو
    car_type_name = models.CharField(max_length=100,default="null")
    used = models.CharField(max_length=64)  # مورد استفاده (شخصی ، تاکسی، مسافربری درون شهری ، مسافربری برون شهری )
    year_of_manufacture = models.IntegerField()  # سال ساخت خودرو
    third_discount = models.IntegerField(default=0)  # درصد تخفیف  مندرج برگه شخص ثالث
    accident_discounts = models.IntegerField(default=0)  # درصد تخفیف بیمه حوادث
    number_of_accidents = models.CharField(max_length=128)  # سوابق خسارت بیمه شخص ثالث
    number_of_incidents = models.CharField(max_length=128)  # سوابق خسارت بیمه حوادث راننده
    expiration_date = jDateField()  # تاریخ انقضا بیمه نامه
    face_image = models.ImageField(upload_to='car/')  # تصویر روی کارت ماشن
    back_image = models.ImageField(upload_to='car/')  # تصویر پشت کارت ماشن
    image_insurance_policy = models.ImageField(upload_to='car/')  # تصویر بیمه نامه قبلی

    def __str__(self):
        return f"{self.user.full_name} - {self.car_type_name}"


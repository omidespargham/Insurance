from django.db import models
from accounts.models import User

class IndividualIncidentsModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    number_people = models.IntegerField()  # تعداد نفرات
    limit_time = models.CharField(max_length=8)  # مدت زمان بیمه (3 ماه ، 6 ماه ،9 ماه ، یک سال)
    job_category = models.CharField(max_length=512) # دسته بندی شغلی شامل موارد زیر


    def __str__(self) :
        return f"user = {self.user} - people = {self.number_people}"
from django.db import models
from accounts.models import User

class IndividualIncidentsModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    number_people = models.IntegerField()  # تعداد نفرات
    limit_time = models.CharField(max_length=8)  # مدت زمان بیمه (3 ماه ، 6 ماه ،9 ماه ، یک سال)
    job_category = models.CharField(max_length=512)
    # job_category = دسته بندی شغلی شامل موارد زیر
    # محصل ، دانشجو یا مدرس
    # مشاغل اداری و دفتری مدیران و کارمندان دولتی و خصوصی
    # فروش و بازاریابی-فروشنده/ بازاریاب /صندوقدار
    # مشاغل خدماتی
    # مشاغل درباره ابزار سبک و تعمیرات
    # کاربامواد شمیایی و قابل اشتعال
    # کارباابزار و ماشین آلات سنگین
    # پزشکان و کادر درمان
    # کاربا برق
    # کار در ارتفاع
    # کاربا اصلحه
    # کاربا ماشین آلان صنعتی
    # خبر نگاری - عکاسی و مشاغل مربوط به حوضه رسانه
    # فعالین حوضه سینما تلوزیون تاتر
    # فعالین گردشگری داخلی و خارجی
    # مسافرت خارجی
    # مسافرت خارجی
    # بدون شغل
    # سایر

    def __str__(self) :
        return f"user = {self.user} - people = {self.number_people}"
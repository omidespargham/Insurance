from django.urls import path

from car.views import RegisterView

app_name = 'car'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register')
]

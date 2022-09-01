from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('contact_us/', views.ContactUsView.as_view(), name="contact_us"),
    path('about_us/', views.AboutUsView.as_view(), name="about_us"),
]

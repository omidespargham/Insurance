from django.urls import path
from Individual_incidents import views

app_name = 'individual_incidents'
urlpatterns = [
    path('register/', views.Individual_Incidents.as_view(), name='register')
]

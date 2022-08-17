from django.urls import path
from Individual_incidents.views import Individual_Incidents

app_name = 'individual_incidents'
urlpatterns = [
    path('', Individual_Incidents.as_view(), name='individual_incidents')
]

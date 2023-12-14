# flight_app/urls.py

from django.urls import path
from .views import flight_map

urlpatterns = [
    path('flight-map/', flight_map, name='flight_map'),
]

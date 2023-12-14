"""
URL configuration for flight_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# flight_tracker/urls.py

# flight_tracker/urls.py

from django.contrib import admin
from django.urls import path, include
from flight_app.views import flight_map  # Import your view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flight-app/', include('flight_app.urls')),
    path('', flight_map, name='home'),  # Add this line for the root path
]

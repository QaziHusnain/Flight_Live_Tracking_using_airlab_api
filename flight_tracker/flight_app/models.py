# flight_app/models.py

from django.db import models

class Flight(models.Model):
    hex = models.CharField(max_length=255)
    flag = models.CharField(max_length=255, null=True)
    lat = models.FloatField()
    lng = models.FloatField()
    dir = models.FloatField()
    alt = models.FloatField(default=0.0)  # Set the default value for Altitude

    def __str__(self):
        return f"Flight {self.hex}"

# flight_app/views.py
from django.db import transaction
from django.shortcuts import render
from .models import Flight
import requests

def fetch_flight_data(api_key):
    api_url = "https://airlabs.co/api/v9/flights"
    params = {
        '_view': 'array',
        '_fields': 'hex,flag,lat,lng,dir,alt',
        'api_key': 'f126f1a8-c312-43fa-a73a-0533d01821ab' # Use the provided parameter instead of hardcoding the key
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Inside the flight_map view function
# Inside the flight_map view function
# Inside the flight_map view function
# Inside the flight_map view function
def flight_map(request):
    api_key = 'f126f1a8-c312-43fa-a73a-0533d01821ab'
    flight_data = fetch_flight_data(api_key)

    # Print the raw API response data for debugging
    for data in flight_data:
        print(data)

    flights = []  # Initialize an empty list to store flight data

    for flight_info in flight_data:
        if isinstance(flight_info, list) and len(flight_info) == 6:
            flight = {
                'hex': flight_info[0],
                'flag': flight_info[1],
                'lat': flight_info[2],
                'lng': flight_info[3],
                'dir': flight_info[4],
                'alt': flight_info[5]
            }
            flights.append(flight)

    print(flights)
    return render(request, 'flight_app/flight_map.html', {'flights': flights})



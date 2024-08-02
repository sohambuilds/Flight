import requests
from flight_data import FlightData

import os
key = os.environ.get("apikey")
class FlightSearch:
     def __init__(self, origin, destination, departure_date):
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date 
    #This cl is responsible for talking to the Flight Search API.

     def search_flights(self):
        url = 'test.api.amadeus.com/v2'
        params = {
            
        "origin": self.origin,
        "destination": self.destination,
        "departure_date": self.departure_date
            



        }

        headers = {"Authorization": f"Bearer {key}"}
        response = requests.get(url,params = params,headers=headers)
        if response.status_code == 200:
            
            data = response.json()
            for flight_data in data:
                flight = FlightData()

            return data;

        else:
            print("Request Failed")

        
    
        pass

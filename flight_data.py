


class FlightData:
    def __init__(self,flight_data):
        self.data = flight_data


     
    #This class is responsible for structuring the flight data.



    pass
    def sort_flights_by_price(self):
        
        return sorted(self.data, key=lambda x: x.price)
    
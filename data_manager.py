import requests
import os



class DataManager:

    def __init__(self,sheetlink):
        self.link = sheetlink


        pass

    def getdata(self):
        url = f'https://api.sheety.co/{self.link}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            return data
        
        else:
            print(f"failed to get data, error code {response.status_code}")

            return None
        

    def push_data(self,flight_data):
        for flight in flight_data:
            iata_code = flight.get('iataCode')
            destination = flight.get('destinationm')
            price = flight.get('price')

            url = f"https://api.sheety.co/self{self.link}"

            data = {
                "key1":{
                    "iataCode": iata_code,
                    "destination": destination,
                    "price": price
                }
            }

            response = requests.post(url,json=data)

            if(response.status_code == 200):
                print(f"Data for {iata_code} pushed successfully")

            else:
                print(f"Error while pushing data for {iata_code}: {response.status_code} {response.text}")

                



    #This class is responsible for talking to the Google Sheet.

    
    pass
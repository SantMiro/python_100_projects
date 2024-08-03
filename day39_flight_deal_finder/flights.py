import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded"
}
DATA = {
    "grant_type": "client_credentials",
    "client_id": os.getenv('AMADEUS_TOKEN'),
    "client_secret": os.getenv('AMADEUS_SECRET') 
}
AMADEUS_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
class FlightDeals():
    def __init__(self):
        self.url = URL
        self.headers = HEADERS
        self.data = DATA
        self.amadeus_url = AMADEUS_URL
        self.max_price = 500
        self.destination = 'CUN'
        self.departure = (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d')
        self.arrival = (datetime.today() + timedelta(days=37)).strftime('%Y-%m-%d')


    def get_acces_token(self):

        response = requests.post(self.url, headers=self.headers, data=self.data)
        if response.status_code == 200:
            token_info = response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
            print(response.text)

        return token_info['access_token']


#print(AMADEUS_ACCESS_TOKEN)#os.getenv('AMADEUS_ACCESS_TOKEN')

    def get_query_parameters(self):
        query = {
                    "originLocationCode": "YYZ",
                    "destinationLocationCode":self.destination,
                    "departureDate": self.departure,
                    "returnDate": self.arrival,
                    "adults": 1,
                    #"nonStop": "true",
                    "currencyCode": "CAD",
                    "max": "10",
                }
        return query

    def get_flight_deals(self):
            
        header = {"Authorization": f"Bearer {self.get_acces_token()}"}
        response = requests.get(url=self.amadeus_url,headers=header,params=self.get_query_parameters())
        response.raise_for_status()
        data = response.json()
        flight_list = self.filter_data(data)
        return flight_list
    
    def filter_data(self,data):
        keys_to_keep = ['source', 'numberOfBookableSeats','itineraries','price']
        flight_list = []
        for element in data['data']:
            if float(element['price']['total']) < self.max_price:
                flight_dict = {}
                for key in keys_to_keep:
                    if key == 'price':
                        flight_dict[key] = element[key]['total']
                    elif key == 'itineraries':
                        flight_dict[key] = []
                        route_n = 0
                        for route in element[key]:
                            for direction in route['segments']:
                                flight_dict[key].append({'departure':direction['departure']['iataCode'],
                                                         'date':direction['departure']['at'],
                                                         'arrival':direction['arrival']['iataCode'],
                                                         'carrierCode':direction['carrierCode'],
                                                         'number':direction['number']})
                    else:
                        flight_dict[key] = element[key]
                if flight_dict:
                    flight_list.append(flight_dict)
        return flight_list
    

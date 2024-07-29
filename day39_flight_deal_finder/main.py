import requests
import os
from dotenv import load_dotenv

load_dotenv()
# FLIGHT_DEALS_TOKEN = os.getenv('FLIGHT_DEALS_TOKEN')
# EXCEL_URL = 'https://api.sheety.co/dfeb845ae19c4c45169cac46b21c9926/flightDeals/deals'
# headers = {"Authorization": f"Bearer {FLIGHT_DEALS_TOKEN}"}
# ID = 5
# response = requests.get(EXCEL_URL + '/' + str(ID))
# #response.raise_for_status()
# data = response.json()
# print(data)

url = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": os.getenv('AMADEUS_TOKEN'),  # Replace with your actual client_id
    "client_secret": os.getenv('AMADEUS_SECRET')  # Replace with your actual client_secret
}

response = requests.post(url, headers=headers, data=data)
if response.status_code == 200:
    token_info = response.json()
    print(token_info)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)

AMADEUS_ACCESS_TOKEN = token_info['access_token']
print(AMADEUS_ACCESS_TOKEN)#os.getenv('AMADEUS_ACCESS_TOKEN')


# headers = {"Authorization": f"Bearer {AMADEUS_ACCESS_TOKEN}"}
# query = {
#     "keyword": 'Paris',
#     "max": "2",
#     "include": "AIRPORTS",
# }
# response = requests.get(
#     url="https://test.api.amadeus.com/v1/reference-data/locations/cities",
#     headers=headers,
#     params=query
# )
# print(f"Status code {response.status_code}. Airport IATA: {response.text}")
AMADEUS_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
query = {
            "originLocationCode": "YYZ",
            "destinationLocationCode": "PAR",
            "departureDate": "2024-10-10",
            "returnDate": "2024-11-10",
            "adults": 1,
            #"nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

header = {"Authorization": f"Bearer {AMADEUS_ACCESS_TOKEN}"}
response = requests.get(url=AMADEUS_URL,headers=header,params=query)
response.raise_for_status()
data = response.json()
print(data)
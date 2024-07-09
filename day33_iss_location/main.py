import requests
import googlemaps
import haversine
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
print('Please add your current corrdinates latitude and longitude: ')
street = '81st ave'
city = 'Edmonton'
state = 'Alberta'
postal_code = 'T6G 0S3'
country = 'Canada'
address = f"{street}, {city}, {state}, {postal_code}, {country}"


gmaps = googlemaps.Client(key=API_KEY)
geocode_result = gmaps.geocode(address)

user_latitude = geocode_result[0]['geometry']['location']['lat']
user_longitude = geocode_result[0]['geometry']['location']['lng']
CURRENT_ADDRESS = (user_latitude, user_longitude)
formatted_address_components = []
response_iss = requests.get(url = "http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()

data_iss = response_iss.json()

latitude = float(data_iss['iss_position']['latitude'])
longitude = float(data_iss['iss_position']['longitude'])

reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
#print(reverse_geocode_result)
for result in reverse_geocode_result:
    formatted_address = result.get('formatted_address')
    if formatted_address:
        formatted_address_components.append(formatted_address)

URL = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={CURRENT_ADDRESS[0]},{CURRENT_ADDRESS[1]}&destinations={latitude},{longitude}&key={API_KEY}'
response = requests.get(URL)
data = response.json()
#print(data)
lat1,long1 = data['destination_addresses'][0].split(',')
lat2,long2 = data['origin_addresses'][0].split(',')
distance = haversine.haversine(float(lat1),float(long1),float(lat2),float(long2))
#print(distance)
if len(formatted_address_components) > 1:
    print(f'The space station is currently over {formatted_address_components[-1]}.')
    
else:
    print('The Space Station is currently over the Ocean. Try again in a few minutes.')

if data['rows'][0]['elements'][0]['status'] == 'ZERO_RESULTS':
    print('There is not a driving route to its current position.')

print(f'Your current distance to the ISS is: {distance:.2f}km.')
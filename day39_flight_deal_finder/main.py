from flights import FlightDeals
from sheets_list import city_list
#from twilio_alert import SendWhats
from dotenv import load_dotenv
import os
load_dotenv()
import requests

AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
#whats_message = SendWhats(account_sid=ACCOUNT_SID,auth_token=AUTH_TOKEN)

querries = city_list()

flights = []
for city in querries:
    flight_deals = FlightDeals()
    flight_deals.max_price = city['lowestPrice']
    flight_deals.destination = city['iataCode']
    best_deal = flight_deals.get_flight_deals()
    if best_deal:
        flights.append(best_deal[0])

if flights:
    for flight in flights:
        text = 'Check the following flight deals: \n\n'
        text += f"There is a flight from {flight['itineraries'][0]['departure']} arriving to {flight['itineraries'][0]['arrival']} at {flight['itineraries'][0]['date']}.\n\n"
        text += f"The total cost is {flight['price']} by {flight['itineraries'][0]['carrierCode']} {flight['itineraries'][0]['number']}.\n\n"
        text += f"The source is {flight['source']}.\n The number of seats is: {flight['numberOfBookableSeats']}.\n"
        print(text)
else:
    print('No good deals right now.')
    #message_sid = whats_message.send_message(flights=flights)

#print(message_sid)
#print(flights)
#print(len(flights))

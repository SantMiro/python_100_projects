from twilio.rest import Client
from dotenv import load_dotenv
import logging
import os
load_dotenv()

FROM_NUMBER = os.getenv('TWILIO_WHATSAPP')
TO_NUMBER = os.getenv('TWILIO_USER_WHATSAPP')

AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')


class SendWhats(Client):
    def __init__(self, account_sid, auth_token):
        super().__init__(account_sid, auth_token)

    
    def send_message(self):
        # for flight in flights:
        #     text = 'Check the following flight deals: \n\n'
        #     text += f"There is a flight from {flight['itineraries'][0]['departure']} arriving to {flight['itineraries'][0]['arrival']} at {flight['itineraries'][0]['date']}.\n\n"
        #     text += f"The total cost is {flight['price']} by {flight['itineraries'][0]['carrierCode']} {flight['itineraries'][0]['number']}.\n\n"
        #     text += f"The source is {flight['source']}.\n The number of seats is: {flight['numberOfBookableSeats']}.\n"
            
            try:
                message = self.messages.create(
                    from_=FROM_NUMBER,
                    body='This is a test',
                    to=TO_NUMBER
                )
                logging.info(f"Message sent successfully. SID: {message.sid}")
                return message.body
            except Exception as e:
                logging.error(f"Failed to send message: {e}")
                return None
            
whats_message = SendWhats(account_sid=ACCOUNT_SID,auth_token=AUTH_TOKEN)

message_sid = whats_message.send_message()

print(message_sid)
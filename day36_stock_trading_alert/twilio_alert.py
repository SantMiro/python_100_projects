from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()

FROM_NUMBER = os.getenv('TWILIO_WHATSAPP')
TO_NUMBER = os.getenv('TWILIO_USER_WHATSAPP')

class SendWhats(Client):
    def __init__(self, account_sid, auth_token):
        super().__init__(account_sid, auth_token)

    
    def send_message(self,articles: list, difference):
        text = "\n\n".join(f"{title}\n{url}" for title, url in articles)
        change = f'There has been a change of {difference} points today.\n\n'
        full_text = change + text
        message = self.messages.create(
            from_=FROM_NUMBER,
            body= full_text,
            to= TO_NUMBER)

        return message.sid
    

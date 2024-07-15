from twilio.rest import Client


class SendWhats(Client):
    def __init__(self, account_sid, auth_token):
        super().__init__(account_sid, auth_token)

    
    def send_message(self,articles: list, difference):
        text = "\n\n".join(f"{title}\n{url}" for title, url in articles)
        change = f'There has been a change of {difference} points today.\n\n'
        full_text = change + text
        message = self.messages.create(
            from_='whatsapp:+14155238886',
            body= full_text,
            to='whatsapp:+18254614692')

        return message.sid
    

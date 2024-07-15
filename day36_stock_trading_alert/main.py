from stock import Stock
from news import News
from twilio_alert import SendWhats

from dotenv import load_dotenv
import os
load_dotenv()

AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
ACCOUNT_SID = 'AC859d7aa359c9e964dd662f78ff156297'

stock = Stock()
news = News()
whats_message = SendWhats(account_sid=ACCOUNT_SID,auth_token=AUTH_TOKEN)

stock.update_symbol('GOOGL')

difference = stock.daily_change()

if difference:
    difference = round(difference,2)
    articles = news.request_headlines()
    message_sid = whats_message.send_message(articles, difference=difference)


print(message_sid)







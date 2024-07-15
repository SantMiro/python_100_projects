from stock import Stock
from news import News
import requests
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

stock = Stock()
news = News()

stock.update_symbol('GOOGL')

difference = stock.daily_change()

if difference:
    articles = news.request_headlines()
    print(articles)







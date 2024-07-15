import requests
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
SYMBOL = 'SLF.TRT'

class Stock():
    def __init__(self) -> None:
        self.apikey = API_KEY
        self.symbol = SYMBOL
        self.function = 'TIME_SERIES_DAILY'
        self.url = 'https://www.alphavantage.co/query'
        self.params = {
            'function': self.function,
            'apikey': self.apikey,
        }
        self.change = 3.

    def request(self):
        try:
            r = requests.get(self.url,params=self.params)
            r.raise_for_status()
        except:
            print('An error ocurred in stock.py')
        else:
            data = r.json()
            return data
    
    def get_symbol(self,keyword):
        self.params['keywords'] = str(keyword)
        self.params['function'] = 'SYMBOL_SEARCH'
        data = self.request()
        del self.params['keywords']
        return data
    
    def update_symbol(self,symbol):
        self.symbol = str(symbol)

    def get_daily_data(self):
        self.params['function'] = 'TIME_SERIES_DAILY'
        self.params['symbol'] = self.symbol
        data = self.request()
        try:
            daily_data = data['Time Series (Daily)']
        except:
            print(data)
        else:
            return daily_data

    def daily_change(self):
        data = self.get_daily_data()
        date_format = "%Y-%m-%d"
        today_date = datetime.strptime('2024-07-10', date_format).date()#datetime.today.date()#
        today_date = today_date.strftime(date_format)
        if today_date in data:
            difference = float(data[today_date]['4. close']) - float(data[today_date]['1. open'])
            if difference > self.change:
                return difference
            else:
                print('No change')

        
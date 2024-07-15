import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv('NEWS_API_KEY')
SOURCES_URL = 'https://newsapi.org/v2/top-headlines/sources'
TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines'

class News:
    def __init__(self) -> None:
        self.apikey = API_KEY
        self.url = TOP_HEADLINES_URL
        self.params = {'apiKey': self.apikey,
                  'languange':'en',

                  }
        self.source_list = []
        self.articles = []

    def request(self):
        try:
            r = requests.get(self.url,params=self.params)
            r.raise_for_status()
        except:
            print('An error ocurred in news.py')
        else:
            data = r.json()
            return data
    
    def request_sources(self):
        self.url = SOURCES_URL
        self.params['country'] = 'us',
        data = self.request()
        sources = data['sources']
        for source in sources:
            self.source_list.append(source['id'])
        del self.params['country']
        return self.source_list
    
    def request_headlines(self) -> list:
        if len(self.source_list) == 0:
            self.url = TOP_HEADLINES_URL
            self.params['country'] = 'us'
            data = self.request()
            self.articles = [(data['articles'][-i]['title'],data['articles'][-i]['url']) for i in range(1,4)]
            del self.params['country']
        else:
            for source in self.source_list:
                self.params['sources'] = source
                data = self.request()
                self.articles.append((data['articles'][-1]['title'],data['articles'][-1]['url']))
                del self.params['sources']
        return self.articles



import requests
from datetime import datetime
import os
from dotenv import load_dotenv

################################
# Title: Habit Tracker         #
# Author: Santiago Miro        #
#       July 2024              #
################################
'''This code posts in a built graph in Pixelia through their API.'''

load_dotenv()

USERNAME = os.getenv('PIXELIA_USERNAME')
TOKEN = os.getenv('PIXELIA_TOKEN')
GRAPH_ID = "graph01"

pixela_endpoint = 'https://pixe.la/v1/users'

params = {"token":TOKEN,
          "username":USERNAME,
          "agreeTermsOfService":"yes",
          "notMinor":"yes",
          }

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

config = {'id':"graph01",
            'name':'Reading Habit',
            'unit':'pages',
            'type':"int",
            'color':'shibafu',
            }

headers = {
    'X-USER-TOKEN':TOKEN
}
# response = requests.post(url=graph_endpoint, json=config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
date_format = "%Y%m%d"

today = datetime.now().date().strftime(date_format)

post_request = {'date':today,
                'quantity':'20',
                }

response = requests.post(url=post_endpoint, json=post_request, headers=headers)
print(response.text)
import requests

URL = 'https://api.sheety.co/dfeb845ae19c4c45169cac46b21c9926/flightDeals/deals'

def city_list():
    response = requests.get(URL)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        #print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

    querries = []
    for city in data['deals']:
        dic = {"iataCode":city['iataCode'],
            "lowestPrice":city['lowestPrice']
            }
        querries.append(dic)
    return querries
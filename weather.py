import requests
import requests_cache
import time
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

api_key = os.getenv('weather_token')
city = input("Enter the city name eg. Cairo, New York, London etc: ") or "Beni Suef"
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

# create a api cache that lasts for 10 minutes
requests_cache.install_cache("weather_api_cache",expire_after=600)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if response.from_cache:
        print('Data is from cache')
    else:
        print('API connected successfully')
    print(data["location"]["name"],":",data["current"]["temp_c"],"°C",data["current"]["condition"]["text"])

else:
    print("error",response.status_code)

# call the api again after 10 minutes
# while True:
#     response = requests.get(url)
#     time.sleep(600)

    

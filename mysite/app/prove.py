import requests

# api_key = "21a80af226771c512fda9aa0a28d0b9b"
# user_data= "Tirana"
# response = requests.get(
#         f"https://api.openweathermap.org/data/2.5/weather?q={user_data}&units=imperial&APPID={api_key}")
api_key = "21a80af226771c512fda9aa0a28d0b9b"
city= "Tirana"
current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"

response = requests.get(current_weather_url.format(city, api_key)).json()

current_weather_url2 = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'


lat, lon = response['coord']['lat'], response['coord']['lon']
forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()



# print(response.json())
print("------------------------------")
# print(forecast_response)

# {'coord': {'lon': 19.8189, 'lat': 41.3275}, 
#  'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 
#  'base': 'stations', 'main': {'temp': 72.48, 'feels_like': 73.56, 'temp_min': 72.48, 'temp_max': 72.48, 'pressure': 1016, 'humidity': 88}, 
#  'visibility': 10000, 'wind': {'speed': 3.44, 'deg': 170}, 'clouds': {'all': 0}, 'dt': 1718744899, 'sys': {'type': 1, 'id': 6359, 'country': 'AL', 'sunrise': 1718680030, 'sunset': 1718734601}, 
#  'timezone': 7200, 'id': 3183875, 'name': 'Tirana', 'cod': 200}



from urllib.request import urlopen
import json

url = 'https://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
print(data['city'])





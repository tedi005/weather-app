import requests
import datetime
from urllib.request import urlopen
import json
import math

api_key = '21a80af226771c512fda9aa0a28d0b9b'
current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
city = 'Tirana'


response = requests.get(current_weather_url.format(city, api_key)).json()
print(response)


weather_data = {
    'city': response['name'],
    'temperature': response['main']['temp'],
    'description': response['weather'][0]['description'],
    'icon': response['weather'][0]['icon'],
    'country': response['sys']['country'],
    'feels_like': response['main']['feels_like'],
    'temp_min': response['main']['temp_min'],
    'temp_max': response['main']['temp_max'],
    'visibility': round(response['visibility'] // 1000, 2),
    'pressure': response['main']['pressure'],
    'humidity': response['main']['humidity'],
    'wind_speed': response['wind']['speed'],
    'wind_deg': response['wind']['deg'],
    'clouds': response['clouds']['all'],
    'lat': response['coord']['lat'], 
    'lon': response['coord']['lon'],
    # },
    # 'timezone': response['timezone']
}


import math
from datetime import datetime, timedelta
import pytz
from timezonefinder import TimezoneFinder

def calculate_timezone_offset(longitude):
    # Divide the longitude by 15 to get the raw offset in hours
    raw_offset = longitude / 15
    
    # Take the floor of the result to get the nearest hour
    nearest_hour = math.floor(raw_offset)
    
    # Adjust the result to be within the range of -12 to 12
    if nearest_hour < -12:
        nearest_hour += 24
    elif nearest_hour > 12:
        nearest_hour -= 24
    
    return nearest_hour

def calculate_local_time(latitude, longitude):
    # Calculate the timezone offset
    timezone_offset = calculate_timezone_offset(longitude)
    
    # Get the current UTC time
    utc_time = datetime.utcnow()
    
    # Calculate the local time by adding the timezone offset
    local_time = utc_time + timedelta(hours=timezone_offset)
    
    # Adjust for DST using timezonefinder and pytz
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=latitude, lng=longitude)
    
    if timezone_str:
        timezone = pytz.timezone(timezone_str)
        local_time = timezone.localize(local_time)
        local_time = local_time.astimezone(timezone)
    
    # Format the local time to show time and AM/PM
    formatted_time = local_time.strftime('%I:%M %p')
    
    return formatted_time

# Example usage:
latitude = 40.7128   # Latitude of New York City
longitude = -74.0060 # Longitude of New York City

local_time = calculate_local_time(latitude, longitude)
print(f"time: {local_time}")






# # Function to convert Unix timestamp to human-readable time
# def convert_unix_timestamp(unix_timestamp, timezone_offset):
#     # Convert Unix timestamp to datetime object
#     utc_time = datetime.datetime.utcfromtimestamp(unix_timestamp)
#     # Apply timezone offset
#     local_time = utc_time + datetime.timedelta(seconds=timezone_offset)
#     return local_time.strftime('%Y-%m-%d %H:%M')

# # Extract data from API response
# dt = response['dt']
# sunrise = response['sys']['sunrise']
# sunset = response['sys']['sunset']
# timezone_offset = response['timezone']

# # Convert timestamps to human-readable format
# current_time = convert_unix_timestamp(dt, timezone_offset)
# sunrise_time = convert_unix_timestamp(sunrise, timezone_offset)
# sunset_time = convert_unix_timestamp(sunset, timezone_offset)

# # Print the times
# print(f"Current Time: {current_time}")
# print(f"Sunrise Time: {sunrise_time}")
# print(f"Sunset Time: {sunset_time}")



"""
{'coord': {'lon': -74.006, 'lat': 40.7143},
 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 
 'base': 'stations', 'main': {'temp': 30.92, 'feels_like': 35.7, 'temp_min': 27.98, 'temp_max': 33.88, 'pressure': 1012, 'humidity': 64, 'sea_level': 1012, 'grnd_level': 1011}, 
 'visibility': 10000, 'wind': {'speed': 8.23, 'deg': 190, 'gust': 10.8}, 'clouds': {'all': 0}, 'dt': 1720557926, 
 'sys': {'type': 1, 'id': 4610, 'country': 'US', 'sunrise': 1720517607, 'sunset': 1720571327}, 
 'timezone': -14400, 'id': 5128581, 'name': 'New York', 'cod': 200}
"""
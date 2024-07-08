import requests
import datetime

api_key = '21a80af226771c512fda9aa0a28d0b9b'
current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
city = 'New York'


response = requests.get(current_weather_url.format(city, api_key)).json()
print(response)






# Function to convert Unix timestamp to human-readable time
def convert_unix_timestamp(unix_timestamp, timezone_offset):
    # Convert Unix timestamp to datetime object
    utc_time = datetime.datetime.utcfromtimestamp(unix_timestamp)
    # Apply timezone offset
    local_time = utc_time + datetime.timedelta(seconds=timezone_offset)
    return local_time.strftime('%Y-%m-%d %H:%M')

# Extract data from API response
dt = response['dt']
sunrise = response['sys']['sunrise']
sunset = response['sys']['sunset']
timezone_offset = response['timezone']

# Convert timestamps to human-readable format
current_time = convert_unix_timestamp(dt, timezone_offset)
sunrise_time = convert_unix_timestamp(sunrise, timezone_offset)
sunset_time = convert_unix_timestamp(sunset, timezone_offset)

# Print the times
print(f"Current Time: {current_time}")
print(f"Sunrise Time: {sunrise_time}")
print(f"Sunset Time: {sunset_time}")
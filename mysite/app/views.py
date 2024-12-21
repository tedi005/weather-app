from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from urllib.request import urlopen
import json
from pathlib import Path



def index(request):
    api_key_path = Path(__file__).parent / '.file.txt'
    api_key = api_key_path.read_text().strip()
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

    if 'weather_data' not in request.session:
        request.session['weather_data'] = []


    if request.method == 'POST':
        if 'current-location' in request.POST:
            weather_data = current_location_weather(api_key, current_weather_url)
        else:
            city = request.POST['user_data']
            weather_data = fetch_weather(city, api_key, current_weather_url)
        if weather_data:
            weather_data_list = request.session['weather_data']
            if weather_data not in weather_data_list:
                weather_data_list.append(weather_data)
                request.session['weather_data'] = weather_data_list
            else:
                messages.info(request, "City already added!")
        else:
            messages.info(request, "City not found!")
            
        # Redirect to the same page to prevent resub
        return redirect('index')
    
    context = {
        'weather_data': request.session['weather_data'],
        
    }

    return render(request, 'index.html', context)

def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    
    if response.get('cod') != 200:
        return None


    weather_data = {
        'city': response['name'],
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'main': response['weather'][0]['main'],
        'icon': response['weather'][0]['icon'],

        'feels_like': response['main']['feels_like'],
        'temp_min': response['main']['temp_min'],
        'temp_max': response['main']['temp_max'],
        'grnd_level': response['main']['grnd_level'],
        'pressure': response['main']['pressure'],
        'humidity': response['main']['humidity'],
        'sea_level': response['main']['sea_level'],

        'visibility': round(response['visibility'] // 1000, 2),
        'wind_speed': response['wind']['speed'],
        'wind_deg': response['wind']['deg'],

        'clouds': response['clouds']['all'], 
        'timezone': response['timezone'],

        'lat': response['coord']['lat'], 
        'lon': response['coord']['lon'],

        'sunrise': response['sys']['sunrise'],
        'sunset': response['sys']['sunset'],
        'country': response['sys']['country'],


        # 'rain': response['rain']['1hr'],
        'day_date': response['dt']

        
        
   

    }

    return weather_data



# {'coord': {'lon': 19.8189, 'lat': 41.3275}, 
# 'weather': [{'id': 502, 'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10n'}], 
# 'base': 'stations', 
# 'main': {'temp': 281.64, 'feels_like': 280.53, 'temp_min': 281.64, 'temp_max': 281.64, 'pressure': 1006, 'humidity': 81, 'sea_level': 1006, 'grnd_level': 969}, 
# 'visibility': 10000, 
# 'wind': {'speed': 2.06, 'deg': 260}, 
# 'rain': {'1h': 5.21}, 'clouds': {'all': 75}, 'dt': 1734732535, 
# 'sys': {'type': 1, 'id': 6359, 'country': 'AL', 'sunrise': 1734674572, 'sunset': 1734707640}, 
# 'timezone': 3600, 'id': 3183875, 'name': 'Tirana', 'cod': 200}




def delete_item(request, city):
    if request.method == 'POST':
        weather_data = request.session.get('weather_data', [])
        updated_weather_data = [weather for weather in weather_data if weather['city'] != city]
        request.session['weather_data'] = updated_weather_data
        return redirect('index')
    
    # Handle GET request to show the delete confirmation page
    return render(request, 'weather.html', {'city': city})


def current_location_weather(api_key, current_weather_url):
    try:
        url = 'https://ipinfo.io/json'
        response = urlopen(url)
        location_data = json.load(response)
        city = location_data.get('city')
        if city:
            return fetch_weather(city, api_key, current_weather_url)
        else:
            return None
    except Exception as e:
        return None



# def see_more(request):
#     weather_data_list = request.session.get('weather_data', [])
#     detailed_data = [weather for weather in weather_data_list if weather]
    
#     if detailed_data:
#         # return render(request, 'weather.html', {'city': city, 'weather_data2': detailed_data})
#         return render(request, 'weather.html', {'weather_data2': detailed_data})
#     else:
#         messages.info(request, "No detailed data found for this city.")
#         return redirect('index')
#         # messages.info(request, "No detailed data found for this city.")
#         # return redirect('index')







# def prove(request):
#     weather_data_list = request.session.get('weather_data', [])
#     detailed_data = [weather for weather in weather_data_list]
    
#     if detailed_data:
#         # return render(request, 'weather.html', {'city': city, 'weather_data2': detailed_data})
#         return render(request, 'prove.html', {'weather_data': detailed_data})
#     # else:
#     #     messages.info(request, "No detailed data found for this city.")
#     #     return redirect('index')



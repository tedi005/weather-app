
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token

from urllib.request import urlopen
import json
from pathlib import Path
import requests





@csrf_protect
def index(request):
    api_key_path = Path(__file__).parent / '.file.txt'
    api_key = api_key_path.read_text().strip()
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

    # Ensure session has 'weather_data' key
    if 'weather_data' not in request.session:
        request.session['weather_data'] = []

    if request.method == 'POST':
        if 'current-location' in request.POST:
            weather_data = current_location_weather(api_key, current_weather_url)
        else:
            city = request.POST.get('user_data', '').strip()
            weather_data = fetch_weather(city, api_key, current_weather_url)

        if weather_data:
            weather_data_list = request.session['weather_data']
            if weather_data not in weather_data_list:
                weather_data_list.append(weather_data)
                request.session['weather_data'] = weather_data_list
                messages.success(request, f"{weather_data['city']} added successfully!")
            # else:
                # messages.info(request, "City already added!")
        else:
            messages.error(request, "City not found!")
        
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        csrf_token = get_token(request)
        delete_url_template = request.build_absolute_uri('/delete/city_placeholder/')
        # return JsonResponse({'weather_data': request.session.get('weather_data', []), 'csrf_token': csrf_token})
        return JsonResponse({'weather_data': request.session['weather_data'], 'csrf_token': csrf_token, 'delete_url_template':delete_url_template})
    else:
        return render(request, 'index.html')



def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    
    if response.get('cod') != 200:
        return None


    weather_data = {
        'city': response['name'],
        'temperature': round(response['main']['temp']),
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

        'day_date': response['dt']        
    }
    return weather_data


def delete_item(request, city):
    if request.method == 'POST':
        weather_data = request.session.get('weather_data', [])
        updated_weather_data = [weather for weather in weather_data if weather['city'] != city]
        request.session['weather_data'] = updated_weather_data
        messages.success(request, "City deleted!")
        return redirect('index')
        
    # Handle GET request to show the delete confirmation page
    return render(request, 'weather.html', {'city': city, })





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



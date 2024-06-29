from django.shortcuts import render, redirect
import requests



from django.contrib import messages

from urllib.request import urlopen
import json

def index(request):
    api_key = '21a80af226771c512fda9aa0a28d0b9b'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if 'weather_data' not in request.session:
        request.session['weather_data'] = []
        

    if request.method == 'POST':
        if 'current-location' in request.POST:
            weather_data = get_current_location_weather(api_key, current_weather_url)
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
            

    context = {
        'weather_data': request.session['weather_data']
        
    }

    return render(request, 'index.html', context)

def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    
    if response.get('cod') != 200:
        return None


    weather_data = {
        'city': response['name'],
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        # other details
        'country': response['sys']['country'],
        'feels_like': round(response['main']['feels_like'] - 273.15, 2),
        'temp_min': round (response['main']['temp_min'] - 273.15, 2),
        'temp_max': round(response['main']['temp_max'] - 273.15, 2),
        'visibility': round(response['visibility'] // 1000),
        'pressure': response['main']['pressure'],
        'humidity': response['main']['humidity'],
        'wind_speed': response['wind']['speed'],
        'wind_deg': response['wind']['deg']

    }

    return weather_data



def delete_item(request, city):
    if not city:
        messages.info(request, "City not found!")
    if request.method == "POST":
        weather_data = request.session.get('weather_data', [])
        updated_weather_data = [weather for weather in weather_data if weather['city'] != city]
        request.session['weather_data'] = updated_weather_data
        return redirect('index')
    else:
        return render(request, 'delete.html', {'city': city})


def get_current_location_weather(api_key, current_weather_url):
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
        print(f"Error fetching current location weather: {e}")
        return None



def see_more(request, city):
    weather_data_list = request.session.get('weather_data', [])
    detailed_data = next((weather for weather in weather_data_list if weather['city'] == city), None)
    
    if detailed_data:
        return render(request, 'see_more.html', {'weather_data': detailed_data})
    else:
        messages.info(request, "No detailed data found for this city.")
        return redirect('index')














from django.shortcuts import render, redirect
import requests
import datetime


from django.contrib import messages
# from django.urls import reverse
from django.http import Http404

def index(request):
    api_key = '21a80af226771c512fda9aa0a28d0b9b'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if 'weather_data' not in request.session:
        request.session['weather_data'] = []

    if request.method == 'POST':
        city = request.POST['user_data']
        weather_data = fetch_weather(city, api_key, current_weather_url)
        if weather_data:
            weather_data_list = request.session['weather_data']
            if weather_data not in weather_data_list:
                weather_data_list.append(weather_data)
                request.session['weather_data'] = weather_data_list

            else:
                messages.info(request, "City already added!")
                weather_data = None
        else:
            messages.info(request, "City not found!")
            weather_data = None

    context = {
        'weather_data': request.session['weather_data']
        
    }

    return render(request, 'index.html', context)

def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    
    if response.get('cod') != 200:
        return None


    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    return weather_data

def cancel_dublicate_request(request):
    pass




def delete_item(request, city):
    if not city:
        raise Http404("City not found")
    if request.method == "POST":
        weather_data = request.session.get('weather_data', [])
        updated_weather_data = [weather for weather in weather_data if weather['city'] != city]
        request.session['weather_data'] = updated_weather_data
        return redirect('index')
    else:
        return render(request, 'delete.html', {'city': city})




















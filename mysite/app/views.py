from django.shortcuts import render, redirect
import requests
import datetime
from django.http import HttpResponse
from requests.exceptions import RequestException
from .models import City
from .forms import CityForm


from django.contrib import messages 

def index2(request):
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
                messages.info(request, messages.INFO, "city already added!") # NEED TO FIX THIS ONE
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
    weather_data = request.session.get('weather_data', [])
    updated_weather_data = [weather for weather in weather_data if weather['city'] != city]
    request.session['weather_data'] = updated_weather_data
    return redirect('index') 
    # if 'weather_data' in request.session:
    #     weather_data_list = request.session['weather_data']
    #     for weather_data in weather_data_list:
    #         if weather_data['city'] == city:


    
# def home(request):
#     url = ''
#     err_msg = ''
#     message = ''
#     message_class = ''
#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         if form.is_valid():
#             new_city = form.cleaned_data['name']
#             existing_city_count = City.objects.filter(name=new_city).count()
#             if existing_city_count == 0:
#                 r = requests.get(url.format(new_city)).json()
#                 if r['cod'] == 200:
#                     form.save()
#                 else:
#                     err_msg = 'City does not exist!'
#             else:
#                 err_msg = 'City already exists!'
#         if err_msg:
#             message = err_msg
#             message_class = 'is-danger'
#         else:
#             message = 'City added Successfully!'
#             message_class = 'is_success'
    
#     form = CityForm()
#     cities = City.objects.all()
#     weather_data = []
#     for city in cities:
#         r = requests.get(url.format(city)).json()
#         city_weather = {
#             'city' : city.name,
#             'temperature' : r['main']['temp'],
#             'description' : r['weather'][0]['description'],
#             'icon' : r['weather'][0]['icon'],
#         }
#         weather_data.append(city_weather)
#     context = {
#         'weather_data' : weather_data, 
#         'form' : form,
#         'message' : message,
#         'message_class' : message_class
#         }
#     return render(request,'weather/weather.html', context)









# def delete_city(requests, city_name):
#     City.objects.get(name=city_name).delete()
#     return redirect('home')
def index(request):
    api_key = '21a80af226771c512fda9aa0a28d0b9b'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    # forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'

    if request.method == 'POST':
        city1 = request.POST['user_data']

        weather_data= fetch_weather_and_forecast(city1, api_key, current_weather_url)

        context = {
            'weather_data': weather_data
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def fetch_weather_and_forecast(city, api_key, current_weather_url):#, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }


    return weather_data
























    # daily_forecasts = []
    # for daily_data in forecast_response:
    #     daily_forecasts.append({
    #         # 'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime('%A'),
    #         'min_temp': round(daily_data['temp']['min'] - 273.15, 2),
    #         'max_temp': round(daily_data['temp']['max'] - 273.15, 2),
    #         'description': daily_data['weather'][0]['description'],
    #         'icon': daily_data['weather'][0]['icon'],
    #     })

    
    
#    daily_forecasts

# def home(request):
#     api_key = "21a80af226771c512fda9aa0a28d0b9b"
#     #  current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
#     # forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'

#     weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
#     forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"


#     if request.method == 'POST':
#         user_data = request.POST['user_data']

        
#         weather_data1, daily_forecast1, = get_weather(user_data, api_key, weather_url, forecast_url)

#         context = {
#             "weather_data1": weather_data1,
#             "daily_forecast": daily_forecast1

#         }
#         return render(request, "home.html", context)
#     else:
#         return render(request, "home.html")
    


# def get_weather(location, api_key, weather_url, forecast_url):
#     response = requests.get(weather_url.format(location, api_key)).json()
#     lat, lon = response['coord']['lat'], response['coord']['lon']
#     forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()




#     weather_data = {
#         "city": location,
#         "temperature": round(response['main']['temp'] - 273.15, 2),
#         "description": response['weather'][0]['description'],
#         "icon": response['weather'][0]['icon']
#     }

#     daily_forecasts = []
#     for daily_data in forecast_response['daily'][:5]:
#         daily_forecasts.append({
#             'day':datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
#             'min_temp': round(daily_data['temp']['min'] - 273.15, 2),
#             'max_temp': round(daily_data['temp']['max'] - 273.15, 2),
#             'description': daily_data['weather'][0]['description'],
#             'icon': daily_data['weather'][0]['icon']
#         })


#     return weather_data, daily_forecasts



"""
{'coord': {'lon': 19.8189, 'lat': 41.3275},
'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 
'base': 'stations', 'main': {'temp': 68.88, 'feels_like': 69.37, 'temp_min': 68.88, 'temp_max': 68.88, 'pressure': 1016, 'humidity': 83}, 
'visibility': 10000, 'wind': {'speed': 3.44, 'deg': 150}, 'clouds': {'all': 0}, 'dt': 1718657431, 
'sys': {'type': 1, 'id': 6359, 'country': 'AL', 'sunrise': 1718593624, 'sunset': 1718648183}, 'timezone': 7200, 'id': 3183875, 'name': 'Tirana', 'cod': 200}
"""


  
# def get_weather(request):
#     if request.method == 'POST':
#         user_data= request.GET.get("user_input")
#         if user_data:  # Check if the search bar is filled
#             api_key = "21a80af226771c512fda9aa0a28d0b9b"
#             url = f"https://api.openweathermap.org/data/2.5/weather"

#             try:
#                 #make the api request
#                 response = requests.get(url, params={
#                         'q': user_data,
#                         'units': 'imperial',
#                         'APPID': api_key
#                 })


#                 response.raise_for_status()  # Raise an exception for HTTP errors

#                 # Attempt to parse the response as JSON
#                 data = response.json()

#                 # Process and render the data
#                 return render(request, 'base.html', {'data': data})

#             except RequestException as e:
#                 # Handle network-related errors
#                 return HttpResponse(f'Network error: {str(e)}')
#             except ValueError as e:
#                 # Handle JSON decoding errors
#                 return HttpResponse(f'JSON decoding error: {str(e)}')


#         else:
#                 # If the search bar is empty, return an error message
#                 error = "Please enter a search query."
#                 return render(request, 'home.html', {'error': error})


#     return render(request, 'result.html')



    # if request.method == 'POST':
    #     user_data= request.GET.get("user_input")
    #     api_key = "21a80af226771c512fda9aa0a28d0b9b"
        
    #     # Make the API request
    #     response = requests.get(
    #     f"https://api.openweathermap.org/data/2.5/weather?q={user_data}&units=imperial&APPID={api_key}")
        

    #     if response.status_code == 200:
    #         data = response.json()
    #         # Store the results in the session
    #         request.session['search_results'] = data

    #         return render(request, 'base.html', {'data': data})
    #     else:
    #         # data = {'error': "Not Found"}
    #         return HttpResponse(f'Error: {response.status_code}')
   
    # return render(request, 'base.html')

    

# def delete_data(request):
#     if request.method == 'POST':
#         # Clear the session data
#         if 'search_results' in request.session:
#             del request.session['search_results']
#         return HttpResponse("Data removed successfully.")
    
#     return redirect('search')
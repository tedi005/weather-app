def weather_data_processor(request):
    return {'weather_data': request.session.get('weather_data', [])}
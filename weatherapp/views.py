from django.shortcuts import render
import requests
import datetime

def home(request):
    # 1. Safely check if 'city' was submitted via POST, otherwise default to 'London'
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'London'

    # 2. Added 'units=metric' directly into the URL string for safety
    api_key = "69576f61e92522d5d8d800391725ec86"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

    # 3. Make the request
    response = requests.get(url)
    data = response.json()

    # (Optional safety check just in case the city name is invalid)
    if response.status_code != 200:
        context = {'error': 'City not found or API error!', 'day': datetime.datetime.now()}
        return render(request, 'weatherapp/home.html', context)

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    
    # Note: OpenWeather standard weather API doesn't include 'aqi' in 'main'. 
    # If you want AQI, you'll need a separate API call. Removed to prevent crashes.

    day = datetime.datetime.now()

    context = {
        'description': description,
        'icon': icon,
        'temprature': temp,
        'day': day,
        'city': city
    }

    return render(request, 'homepage/home.html', context)
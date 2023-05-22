from django.shortcuts import render
import requests
import os
from .models import City
from .forms import CityForm

def index(request):
    path = os.getcwd()
    # with open('api keys.txt', "r") as f:
    #     key = f.read()
    key = '883ec61da0091bad56e02f3098eb0550'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + key

    cities = City.objects.all()

    if request.method == 'POST': 
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:


        city_weather = requests.get(url.format(city)).json()        

        weather =  {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        
        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}


    return render(request, 'weather/index.html', context)


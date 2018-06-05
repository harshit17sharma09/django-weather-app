# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
# Create your views here.
from .models import City
from .forms import CityForm


def index(request):
    cities = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9e6e16a9f964855277135cb17e127a63'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon'        : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    

    context ={
        'weather_data' : weather_data , 'form' : form

    }
    return render(request,'weather_report/index.html',context)
    
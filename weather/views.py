from django.shortcuts import render
from django.http import HttpResponse
import requests
from pprint import pprint
import datetime

api_key = 'enter api key from openweather'
city = None


def start(request):
    return render(request, template_name='index.html')



def get_city(request):
    code_to_smile = {
        "Clear": "Sun \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1 ",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist 🌁"
    }

    if request.method == 'GET':
        city = request.GET['typecity']


        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        )
        data = r.json()
        if data["cod"] == '404' or data["cod"] == '400':
            return render(request, template_name='index.html', context={'error': "Sorry, your city not found"})
        else:

            temp = data["main"]["temp"]
            feels_temp = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressur = data["main"]["pressure"]
            pressure = round(pressur * 0.0145, 2)
            speed_of_wind = data["wind"]["speed"]
            country = data["sys"]["country"]
            time = datetime.datetime.now()

            weather_description = data["weather"][0]["main"]
            if weather_description in code_to_smile:
                weather = code_to_smile[weather_description]
            else:
                weather = "I don't know"



    #        print(f"{temp}\n"
    #            f"{feels_temp}\n"
    #            f"{humidity}\n"
    #            f"{pressure}\n"
    #            f"{weather}\n"
    #            f"{speed_of_wind}\n"
    #            f"{country}\n"
    #            )


            return render(request, template_name='index.html',
                          context={'city': city,
                                   'temp': temp,
                                   'feels_temp': feels_temp,
                                   'time': time,
                                   'humidity': humidity,
                                   'pressure': pressure,
                                   'weather': weather,
                                   'speed_of_wind': speed_of_wind,
                                   'country': country})








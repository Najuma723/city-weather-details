# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1go4Hi4Ad977auKS8a4ZgEIak0V4AIDBz
"""

import requests
import datetime

api_key = 'a0fd1838c93081406242ec1a40d7611a'
city = input('Enter the city: ')
api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,api_key)
try :
    response = requests.get(api_url)
except Exception as e :
    print('Error occured while connecting: {}'.format(e))

if response.ok :
    print('Connection Successful............')
    content = response.json()
    date = str(datetime.datetime.now())
    location = city
    temperature = round(content['main']['temp']-273.15,2)
    weather= content['weather'][0]['description']
    humidity = content['main']['humidity']
    wind_speed = content['wind']['speed']
    print(' date: {}\n location: {}\n temperature: {}\n weather: {}\n humidity: {}\n wind_speed: {}'.format(date,location,temperature,weather,humidity,wind_speed))

try :
    f = open("log.txt", "a+")
    f.write('---> date: {}, location: {}, temperature: {}, weather: {}, humidity: {}, wind_speed: {}\n'.format(date,location,temperature,weather,humidity,wind_speed))
    print('Look for the log.txt file for the reviweing the information and log.\n')
    f.close()
except Exception as file_error :
    print("Error while opening the file: {}".format(file_error))
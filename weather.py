import time

import random
import requests
import schedule
from twilio.rest import Client

import dateCondition
import keys
import quote

appid = '' #API key from openWeatherAPI
city = 'New York'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'

r = requests.get(URL)
res = r.json()
data = res

def ran(): #randomly pick from the [] in quote.py
    random.choice(quote.nouns)
    random.choice(quote.morning_quotes)
    random.choice(quote.endWord)


def checkTemp():
    temp = res["main"]["temp"]  # current temp
    condition = res['weather'][0]['main']
    temp_max = res['main']['temp_max']
    temp_min = res['main']['temp_min']

    averageTemp = (temp_max + temp_min) / 2
    averageTemp = int(averageTemp)  # change type from float to int

    if -20 < temp < 4:
        return "{morning_quotes} {nouns},{date},Today = {condition}, {city} average temperature = {averageTemp}°C,super cold 🥶,wear more clothes,{end}".format(
            condition=condition, averageTemp=averageTemp, morning_quotes=random.choice(quote.morning_quotes),
            nouns=random.choice(quote.nouns), date=dateCondition.dateCondition(), end=random.choice(quote.endWord),
            city=city)
    elif 4 < temp < 11:
        return "{morning_quotes} {nouns},date},Today  = {condition}, {city} average temperature = {averageTemp}°C,very cold,wear big jacket,{end}".format(
            condition=condition, averageTemp=averageTemp, morning_quotes=random.choice(quote.morning_quotes),
            nouns=random.choice(quote.nouns), date=dateCondition.dateCondition(), end=random.choice(quote.endWord),
            city=city)
    elif 11 < temp < 15:
        return "{morning_quotes} {nouns},{date},Today  = {condition}, {city} average temperature = {averageTemp}°C,little cold,wear jacket,{end}".format(
            condition=condition, averageTemp=averageTemp, morning_quotes=random.choice(quote.morning_quotes),
            nouns=random.choice(quote.nouns), date=dateCondition.dateCondition(), end=random.choice(quote.endWord),
            city=city)
    elif 15 < temp < 20:
        return "{morning_quotes} {nouns},{date},Today  = {condition}, {city} average temperature ={averageTemp}°C,little warm,wear normal,{end} ".format(
            condition=condition, averageTemp=averageTemp, morning_quotes=random.choice(quote.morning_quotes),
            nouns=random.choice(quote.nouns), date=dateCondition.dateCondition(), end=random.choice(quote.endWord),
            city=city)
    elif 20 < temp < 25:
        return "{morning_quotes} {nouns},{date},Today  = {condition}, {city} average temperature ={averageTemp}°C,warm day 😌,wear what you want,{end}".format(
            condition=condition, averageTemp=averageTemp, morning_quotes=random.choice(quote.morning_quotes),
            nouns=random.choice(quote.nouns), date=dateCondition.dateCondition(), end=random.choice(quote.endWord),
            city=city)
    elif 25 < temp < 30:
        return "{morning_quotes} {nouns},{date},Today  = {condition}, {city} average temperature = {averageTemp}°C,very hot 🥵 drink more water,{end}".format(
            condition=condition, averageTemp=averageTemp, morning_quotes=random.choice(quote.morning_quotes),
            nouns=random.choice(quote.nouns), date=dateCondition.dateCondition(), end=random.choice(quote.endWord),
            city=city)
    elif 31 < temp < 45:
        return "{morning_quotes} {nouns},{date},Today  = {condition}, {city} average temperature = {averageTemp}°C，super hot 🔥,drink more water{end}".format(
            condition=condition, averageTemp=averageTemp, morning_quotes=random.choice(quote.morning_quotes),
            nouns=random.choice(quote.nouns), date=dateCondition.dateCondition(), end=random.choice(quote.endWord),
            city=city)
    else:
        return "{morning_quotes} {nouns},{date},Today  = {condition},{city} average temperature = {averageTemp}°C ，{end}".format(
            condition=condition, averageTemp=averageTemp, morning_quotes=random.choice(quote.morning_quotes),
            nouns=random.choice(quote.nouns), date=dateCondition.dateCondition(), end=random.choice(quote.endWord),
            city=city)


checkTemp()


def send_message(): #twilio message
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
        body=checkTemp(),
        from_=keys.twilio_number,
        to=keys.target_number)

    print(message.body)


schedule.every().day.at("07:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(2)

import requests

city = input()

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    "q": city,
    "units": "metric",
    "lang": "ru",
    'appid': '79d1ca96933b0328e1c7e3e7a26cb347'
}
response = requests.get(url, params=params).json()

print(response['main']['temp'])
temp = round(response['main']['temp'])
temp_feel = round(response['main']['feels_like'])
wind_speed = response['wind']['speed']
wind_deg = response['wind']['deg']
direction = wind_deg
if wind_deg < 22.5 or wind_deg > 337.5:
    direction = 'С'
elif wind_deg < 67.5:
    direction = 'СВ'
elif wind_deg < 112.5:
    direction = 'В'
elif wind_deg < 157.5:
    direction = 'ЮВ'
elif wind_deg < 202.5:
    direction = 'Ю'
elif wind_deg < 247.5:
    direction = 'ЮЗ'
elif wind_deg < 292.5:
    direction = 'З'
else:
    direction = 'СЗ'

pressure = response['main']['pressure']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
print(f"Погода в {response['name']}:\n-Температура: {temp}°C (ощущается как {temp_feel}°C)\n-Ветер: {wind_speed}м/с"
    + f" {direction}\n-Давление: {round(pressure*3/4)}мм рт.ст.\n-Влажность: {humidity}%\n-{description}")
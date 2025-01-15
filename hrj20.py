#Marcus Krutto harjutus 20
#14.01.2025

import requests

#Küsib kasutajalt
kasutaja = input("Palun sisesta soovitud linn: ").lower()


# API võtme ja linna nime määramine
city = kasutaja
api_key = "b4396cfab559f60963d90d80121ba3f4"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


# API päringu tegemine
response = requests.get(url)


# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Hetke temperatuur: {city.title()} {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)


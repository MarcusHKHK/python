#Marcus Krutto 22.01.25
#Kontrolltöö

# Ühenda andmetega
# Kasutaja sisestab otsitava
# Kuvab otsitavad põhiandmed (2-3tk)

#Import
import requests
import json

#Küsib kasutajalt
kasutaja = input("Palun sisestage märksõna: ")
url = 'https://dummy-json.mock.beeceptor.com/quotes'
response = requests.get(url)

#Faili töötlus
if response.status_code == 200:
    data = response.json()
    for i in data:
        if kasutaja.lower() in i['quote']:
            print(i['quote'])
else:
    print("Viga andmete allalaadimisel:", response.status_code)



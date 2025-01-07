#Python hrj18 Marcus Krutto
#07.01.2025

#Import
import json

# Faili avamine ja JSON-i laadimine
with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    tulemused = json.load(file)

counter12 = 0
counter11 = 0
counter10 = 0

#Faili töötlus
for tulemus in tulemused:
    nimi = tulemus['nimi']
    klass = tulemus['klass']
    if klass == "12":
        counter12+=1
        print(f"{counter12}.{nimi}")
    if klass == "11":
        counter11+=1
        print(f"{counter11}")
    if klass == "10":
        counter10+=1
        print(f"{counter10}")



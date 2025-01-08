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
        print(f"{counter12+1}. {nimi}")
        counter12+=1
    if klass == "11":
        counter11+=1
    if klass == "10":
        counter10+=1

#Õpilaste arv
print(f"10. klass: {counter10}, 11. klass: {counter11}, 12. klass: {counter12}")

#Trennid ja hinded
for tulemus in tulemused:
    nimi = tulemus['nimi']
    klass = tulemus['klass']
    tegevused = tulemus['tegevused']
    hinded = tulemus['hinded']
    tegevused = tulemus['tegevused']
    if klass == "12":
        print(f"{counter12+1}.{nimi}, Hinded: ")
        for k, v in hinded.items():
            print(k, v)
        a = tegevused.join(tegevused)
        print(f"{a}")

        




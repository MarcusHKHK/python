#Marcus Krutto 22.01.25
#Kontrolltöö

# Ühenda andmetega
# Kasutaja sisestab otsitava
# Kuvab otsitavad põhiandmed (2-3tk)

#Import
import requests
import json

#Küsib kasutajalt
print("------------------------POSTITUSED------------------------")
print("Info mida saab küsida:'postitused', 'nimi', 'sisu', 'viited' ja 'andmed'")
kasutaja = input("Mille kohta infot soovite: ").lower()
asi = kasutaja
url = 'https://dummyjson.com/posts'
response = requests.get(url)

#Faili töötlus
if response.status_code == 200:
    data = response.json()
    postitused = data['posts']
    print(f"Andmed mida soovisite: {asi}")
else:
    print("Viga andmete allalaadimisel:", response.status_code)

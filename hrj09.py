#24.10.2024 Marcus Krutto
#ülesanded 9 tsüklid

#import
import random

"""""
#Genereeri ja kuva arvud 1-20

for i in range(1,21):
    print(i, end=" ")
print()

#Genereerija kuva 20 suvalist arvu

for i in range(1, 21):
    print(random.randint(1, 99), end=" ")
print()

#Kasuta loendit

loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud = []

for i in loend:
    if i%2==0:
        paaris.append(i)
    else:
        paaritud.append(i)

print(f"Paaris arvude summa on: {sum(paaris)}")
print(f"Paartute arvude summa on: {sum(paaritud)}")

print()
"""

#kuva arvud 1-42
for i in range(1, 43):
    if i%3==0 and i%5==0:
        print(i, "TIKTAK", end=" ")
    elif i%3==0:
        print(i, "TIK", end=" ")
    elif i%5==0:
        print(i, "Tak", end=" ")
    else:
        print(i, end=" ")


#Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.

jaguneb7 = []

for i in range(200, 321):
    if i%7==0:
        jaguneb7.append(i)



print(jaguneb7)

    









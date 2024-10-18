#16.10.24 Marcus Krutto
#hrj04

import turtle

"""
#1. aia pikkus
a = int(input("Sisesta külg 1: "))
b = int(input("Sisesta külg 2: "))
p = 2 * (a + b)
print(f"Aia kogupikkus on {p} meetrit.")
"""

"""

#Raamatu allahindlus
ale = 0.3
kogus = 3
hind = 12.53
summa = hind - (hind * ale) * kogus
print(f"{kogus} raamatu hind soodustega on {summa:0.2f}€.")

"""


"""""
#Faili allalaadimine
try:
    failisuurus = int(input("Sisesta faili suurus (MB): "))
    downkiirus = int(input("Sisesta allalaadimis kiirus (MB/s): "))
    aeg = failisuurus / downkiirus
    print(f"Allalaadimiseks kulub {aeg:0.2f} sekundit")
except:
    print("Tegid sisestamisel vea!")
"""""

"""""
#Kingituse pakkimine
try:
    Kingitused = int(input("Lisa kinkide arv: "))
    maht = 5
    pakid = Kingitused // maht
    yle = Kingitused % maht
    print(f"Saad teha {pakid} täis kinkekasti. Üle jääb {yle} kingitust")
except:
    print("Tegid sisestamisel vea!")
"""""

#Ringi pindala ja Turtle

try:
    r = int(input("Lisa ringi raadius: "))
    pi = 3.14
    s = pi*r**2
    p = 2*pi*r
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r, 360)
except:
    print("Tegid sisestamisel vea!")




turtle.done










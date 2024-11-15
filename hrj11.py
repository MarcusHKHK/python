#08.11.2024 Marcus Krutto IT-24
#Harjutus 11

import turtle
import random

# def pikim_sõna(*sonad):
#     pikim = 0
#     for i in sonad:
#         if len(i)>pikim:
#             pikim=len(i)
#     print(f"Pikim sõna on {pikim} märki!")



# pikim_sõna("üks", "kaks", "kolmsada", "INFGAIJFBNNEGUIONWR")

# def kolm_pikim_sona(a):
#     sonastik = {}
#     for i in a:
#         sonastik[i] = len(i)
#     sorteeritud = (sorted(sonastik.items(), key = lambda x:x[1], reverse = True))
#     for j in range(3):
#         print(sorteeritud[j])

# sonad = ["üks", "kaks", "kolmskümmend", "viissada", "kaheksasada", "viis"]


# kolm_pikim_sona(sonad)


#Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.

# def sarnased_esitahed(nimi):
#     tykk = nimi.split(" ")
#     if tykk[0][0] == tykk[1][0]:
#         return True
#     else:
#         return False


# print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
# print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False





# Kilpkonn – kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. 
# Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.

def viisnurk(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,90))
        for i in range(5):
            turtle.fd(100)
            turtle.lt(36)
            turtle.fd(100)
            turtle.rt(108)

def ring(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,90))
        for i in range(1):
            turtle.circle(100)

def ruut(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,90))
        for i in range(4):
           turtle.fd(100)
           turtle.lt(90)


def suvaline(k):
    turtle.speed(0)
    for i in range(k):
        valikud = [viisnurk, ring, ruut]
        random.choice(valikud)(1)


print("-------------Minu fancy programm-------------")

loop = 1

while loop==1:
    try:
      valik = int(input("1 - viisnurk\n2 - ring\n3 - ruut\n4 - suvaline\nlisa valik (1-4): "))
      kujunditearv = int(input("Mitu kujundit soovid joonistada: "))
    except:
        print("Game over")
        turtle.bye()
        loop = 0
        break

    if valik =="" or kujunditearv=="":
        print("Game over")
        turtle.bye()
        loop = 0
        break

    if valik == 1:
        viisnurk(kujunditearv)
    elif valik == 2:
        ring(kujunditearv)
    elif valik == 3:
        ruut(kujunditearv)
    elif valik == 4:
        suvaline(kujunditearv)






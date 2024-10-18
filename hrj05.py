#18.10.2024 Marcus Krutto
#Ülesanne 5
import random
import turtle

#Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
#1=kull
#2=kiri

suv = random.randint(0,1)
kasutaja_valik = input("Kull või kiri? ")
if (suv == 1 and kasutaja_valik == "kull") or (suv == 0 and kasutaja_valik == "kiri"):
    varv = "green"
else:
    varv = "red"

turtle.fillcolor(varv)
turtle.color(varv)
turtle.begin_fill()
turtle.end_fill()
turtle.circle(50)
turtle.done()








"""
#Matemaatika test (randiant)
a , b = random.randint(1, 10), random.randint(1, 10)
vastus = int(input(f"{a}*{b} = "))
if vastus == a*b:
    print("Tubli")
else:
    print("Mario palus ütelda, et Loll oled!")





#Ilmaennustuse rakendus
c = -115
if c < 0:
    print("Talveriided")
elif c >= 0 and c <=15:
    print("Kevad-Sügis")
else:
    print("Suvi, miks tahad talveriideid kanda???")




#Vanusepiiranguga üritus
try:
    vanus = 16
    if vanus>=18:
        print("Olete piisavalt vana, et siseneda!")
    else:
        print("Olete liiga noor, palun lahkuge!")
except:
    print("Tegite sisestamisel vea!")

"""
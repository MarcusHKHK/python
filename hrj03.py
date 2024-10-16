#16.10.2024 Marcus Krutto
#hrj03

#ülesanne 3.6: Python Turtle kolmnurk; Ülesanne 3.5: Unistuste auto

#Import
import turtle

"""""
#Kolmnurk
kylje_pikkus = 100
nurk = 120
kujundi_varv = "red"

turtle.color(kujundi_varv)

for i in range(3):
    for i in range(3):
        turtle.forward(kylje_pikkus)
        turtle.left(nurk)

    turtle.penup()
    turtle.forward(kylje_pikkus*1.5)
    turtle.pendown()
"""""
"""""
#Ül3.5: Unistuste auto
mark, mudel = "bmw", "118"
auto = mark+" "+mudel
aasta = 1997
hind = 301.60

print("Minu unistuste auto on", auto, "aastast", aasta, "mille hind on",hind,"eurot.")
"""""
#turtle.done()

#ül3.2 ostunimekiri
toode = "kartul"
kogus = 3
toote_hind = 2

print("Soovin", toode, " ", kogus, ", mille tüki hind on", toote_hind, "eurot.")










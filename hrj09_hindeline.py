#06.11.2024 Marcus Krutto

#Kasuta Python Turtle moodulit, et tsüklite abil luua järgmised kujundid.
#Kasuta muutujaid ja nendevahelisi seoseid, et kujundid oleks skaleeritavad

#minu numbrid: 6, 7, 10

#import

import turtle

turtle.speed(0)

#Number 6:
#Muutuvad arvud
d = 300
f = (d/2.5)
turn = 90

#pensize
turtle.pensize(2)

#paigutus
turtle.penup()
turtle.backward(200+d)
turtle.pendown()

#Kujund kasutades muutuvaid arve
for i in range(4):
    turtle.fd(d)
    turtle.left(turn)
    turtle.fd(f)
    turtle.left(turn)
    turtle.fd(d)
    turtle.left(turn)
    turtle.fd(f)


#Number 7:
#Muutuvad arvud
a = (d/5) 
b = 45

#pensize
turtle.pensize(2)

#paigutus
turtle.penup()
turtle.fd(200+d)
turtle.pendown()

#Kujund kasutades muutuvaid arve
for i in range(8):
    turtle.fd(a)
    turtle.right(turn)
    turtle.fd(d)
    turtle.right(turn)
    turtle.fd(a)
    turtle.right(turn)
    turtle.fd(d)
    turtle.right(turn)
    turtle.fd(a)
    turtle.left(b)


#Kujund 10
#Muutuvad arvud
n = (d-10)
m = (d-20)
y = 10

#paigutus
turtle.penup()
turtle.fd(200+d)
turtle.pendown()

#pensize
turtle.pensize(2)

#Kujund kasutades muutuvaid arve)
for i in range(4):
    turtle.fd(d/2)
    turtle.right(turn)
    turtle.fd(d)
    turtle.right(turn)
    turtle.fd(y)
    turtle.right(turn)
    turtle.fd(n)
    turtle.left(turn)
    turtle.fd(m)
    turtle.left(turn)
    turtle.fd(n)
    turtle.right(turn)
    turtle.fd(y)
    turtle.right(turn)
    turtle.fd(d)
    turtle.right(turn)
    turtle.fd(d/2)
    turtle.left(turn)

#Nool liigub 0;0
turtle.pensize(1)
turtle.penup()
turtle.goto(0,300)


turtle.done()
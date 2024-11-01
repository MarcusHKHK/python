#18.10.2024 Marcus Krutto
#Ülesanne 6

#Import
import turtle
import math

#Redeli joonestamine maja seinast
kordaja = 10
a = math.radians(53)
h = 4.4
x = abs (h / math.tan(a))
c = math.sqrt(h**2 + x**2)

#Turtle liikumine
turtle.fd(x * kordaja)
turtle.lt(90)
turtle.fd(h * kordaja)
turtle.lt(180-37)
turtle.fd(c * kordaja)



turtle.done()


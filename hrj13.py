#Marcus Krutto 15.11.2024
#Harjutus 13

import turtle

screen = turtle.Screen()
t = turtle.Turtle()

nr = 10
t.speed(0)
for i in range(nr*10):
    t.lt(90)
    t.fd(3)
    t.lt(180)
    t.fd(3)
    t.lt(90)
    t.fd(4)
t.goto(0,0)

for i in range(nr+1):
    t.lt(90)
    t.fd(10)
    t.write(i, font=("Arial", 10, "normal"))
    t.lt(180)
    t.fd(10)
    t.lt(90)
    t.fd(10*4)







turtle.done()
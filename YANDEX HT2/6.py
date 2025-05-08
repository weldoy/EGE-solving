from turtle import *

tracer(0)
size = 10
up()
goto(-200, -100)
down()

rt(315)

for i in range(7):
    fd(70*size)
    rt(45)
    fd(41*size)
    rt(135)

up()
for x in range(-30*size, 30*size, size):
    for y in range(-30*size, 30*size, size):
        goto(x, y)
        dot(3)

done()

from turtle import *

b = Turtle()
size = 30
tracer(10)
goto(0, 100)

for i in range(7):
    fd(9*size)
    rt(90)
    fd(16*size)
    rt(90)

up()
fd(3*size)
rt(90)
fd(4*size)
lt(90)
down()

for i in range(4):
    fd(7*size)
    rt(90)
    fd(13*size)
    rt(90)

up()
for x in range(-5*size, 10*size, size):
    for y in range(-25*size, 10*size, size):
        goto(x, y+100)
        dot(3)

done()

from turtle import *

tracer(0)
size = 30

rt(90)
for i in range(7):
    rt(45)
    fd(11*size)
    rt(45)

up()
for x in range(-15*size, 15*size, size):
    for y in range(-15*size, 15*size, size):
        goto(x, y)
        dot(3)


done()

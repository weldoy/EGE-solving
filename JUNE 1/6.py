from turtle import *

tracer(10)
size = 30

rt(30)
for i in range(18):
    fd(11*size)
    rt(120)
    fd(11*size)
    rt(60)

up()
for x in range(-15*size, 15*size, size):
    for y in range(-15*size, 15*size, size):
        goto(x, y)
        dot(3)

done()

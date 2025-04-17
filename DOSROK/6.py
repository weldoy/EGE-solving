from turtle import *

tracer(5)
size = 30

rt(30)
for i in range(3):
    rt(150)
    fd(6*size)
    rt(30)
    fd(12*size)

up()
for x in range(-20*size, 15*size, size):
    for y in range(-20*size, 15*size, size):
        goto(x, y)
        dot(3)

done()

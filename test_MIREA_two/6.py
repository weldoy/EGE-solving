from turtle import *

tracer(10)
size = 5

for i in range(2):
    fd(8*size)
    rt(90)
    fd(18*size)
    rt(90)
up()
for i in range(4):
    rt(90)
    fd(10*size)
    lt(90)
down()
for i in range(2):
    fd(17*size)
    rt(90)
    fd(7*size)
    rt(90)

up()
for x in range(-25*size, 15*size, size):
    for y in range(-25*size, 15*size, size):
        goto(x, y)
        dot(3)

done()

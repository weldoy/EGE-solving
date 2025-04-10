from turtle import *

tracer(0)
size = 5

for i in range(3):
    fd(27*size)
    rt(90)
    fd(12*size)
    rt(90)

up()

fd(4*size)
rt(90)
fd(6*size)
lt(90)

down()

for i in range(4):
    fd(83*size)
    rt(90)
    fd(77*size)
    rt(90)

up()
for x in range(-100*size, 30*size, size):
    for y in range(-30*size, 100*size, size):
        goto(x, y)
        dot(3)

done()

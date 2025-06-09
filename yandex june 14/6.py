from turtle import *

tracer(10)
size = 5
lt(90)
up()

fd(10*size)
down()
for i in range(6):
    fd(50*size)
    rt(90)
    fd(43*size)
    rt(90)

up()
fd(40*size)
rt(90)
fd(40*size)
down()

for i in range(9):
    fd(40*size)
    lt(90)
    fd(20*size)
    lt(90)

up()
for x in range(15*size, 100*size, size):
    for y in range(15*size, 100*size, size):
        goto(x, y)
        dot(3)

done()

from turtle import *

tracer(10000)
size = 20

for i in range(2):
    fd(7*size)
    rt(90)
    fd(18*size)
    rt(90)

up()
bk(-2*size)
rt(90)
fd(9*size)
lt(90)
down()

for i in range(2):
    fd(8*size)
    rt(90)
    fd(5*size)
    rt(90)

up()
for x in range(-15*size, 15*size, size):
    for y in range(-25*size, 15*size, size):
        goto(x, y)
        dot(3)

done()

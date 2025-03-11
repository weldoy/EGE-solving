from turtle import *
a = Turtle()
size = 15
tracer(10)

for i in range(4):
    fd(10*size)
    rt(270)
up()
fd(3*size)
rt(270)
fd(5*size)
rt(90)
down()

for i in range(2):
    fd(10*size)
    rt(270)
    fd(12*size)
    rt(270)

up()
for x in range(-5*size, 20*size, size):
    for y in range(-5*size, 20*size, size):
        goto(x, y)
        dot(3)

done()

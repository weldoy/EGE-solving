from turtle import *

b = Turtle()
tracer(0)
size = 20
up()
goto(-50, 50)
down()

for i in range(10):
    fd(22*size)
    rt(90)
    fd(16*size)
    rt(90)

up()
fd(1*size)
rt(90)
fd(1*size)
lt(90)
down()

for i in range(10):
    fd(72*size)
    rt(90)
    fd(79*size)
    rt(90)

up()
for x in range(-50*size, 50*size, size):
    for y in range(-50*size, 50*size, size):
        goto(x+50, y-50)
        dot(3)

done()

from turtle import *

tracer(100)
size = 5
up()
goto(-100, 200)
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
for x in range(-100*size, 100*size, size):
    for y in range(-100*size, 100*size, size):
        goto(x, y)
        dot(3)

done()

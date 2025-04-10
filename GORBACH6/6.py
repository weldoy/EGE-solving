from turtle import *

tracer(10)
size = 25

for i in range(4):
    lt(45)
    fd(5*size)
    lt(45)
    fd(6*size)

up()
for x in range(-15*size, 15*size, size):
    for y in range(-15*size, 15*size, size):
        goto(x, y)
        dot(3)

done()

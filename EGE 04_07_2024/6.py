from turtle import *

b = Turtle()

size = 10
# tracer(0)
b.rt(90)

for i in range(2):
    b.fd(19*size)
    b.rt(90)
    b.fd(30 * size)
    b.rt(90)

b.up()

b.fd(2*size)
b.rt(90)
b.fd(8*size)
b.lt(90)

b.down()

for i in range(2):
    b.fd(93*size)
    b.rt(90)
    b.fd(97*size)
    b.rt(90)

exitonclick()

from turtle import *

b = Turtle()
size = 1
tracer(1)

rt(45)
for i in range(10):
    rt(45)
    fd(203*size)
    rt(45)

up()
back(40*size)
rt(45)
down()

for i in range(5):
    fd(20*size)
    lt(90)

# up()
# for x in range(-5*size, 10*size, size):
#     for y in range(-25*size, 10*size, size):
#         goto(x, y)
#         dot(3)

done()

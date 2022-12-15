from turtle import *
screensize(10000, 10000)
left(90)
tracer(0)
k = 20

for i in range(2):
    fd(10 * k)
    right(90)
    fd(20 * k)
    right(90)
up()
fd(3 * k)
right(90)
fd(5 * k)
left(90)
down()
for i in range(2):
    fd(70 * k)
    right(90)
    fd(80 * k)
    right(90)

up()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(5, 'blue')


update()
exitonclick()
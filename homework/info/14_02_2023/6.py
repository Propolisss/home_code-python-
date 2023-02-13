from turtle import *
tracer(0)
k = 20
screensize(10000, 10000)
left(90)

for i in range(6):
    fd(5 * k)
    right(60)
up()
fd(5 * k)
right(90)
down()
for i in range(2):
    fd(15 * k)
    right(90)
    fd(5 * k)
    right(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')


update()
exitonclick()
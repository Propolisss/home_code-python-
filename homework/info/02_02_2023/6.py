from turtle import *
tracer(0)
k = 40
screensize(10000, 10000)
left(90)

for i in range(7):
    fd(10 * k)
    right(120)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')


update()
exitonclick()
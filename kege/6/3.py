from turtle import *
tracer(0)
k = 40
screensize(10000, 10000)

for i in range(11):
    fd(4 * k)
    right(60)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')

update()
exitonclick()
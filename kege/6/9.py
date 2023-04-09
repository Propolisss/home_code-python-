from turtle import *
tracer(0)
k = 40
screensize(10000, 10000)
left(90)

for i in range(10):
    goto(xcor() + 3 * k, ycor() + 6 * k)
    goto(xcor() + 7 * k, ycor() - 2 * k)
    goto(xcor() - 10 * k, ycor() - 4 * k)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')


update()
exitonclick()
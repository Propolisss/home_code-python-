from turtle import *
tracer(0)
screensize(10000, 10000)
left(90)
k = 20

for x in range(3):
    goto(xcor() - 3 * k, ycor() - 4 * k)
    goto(xcor() - 12 * k, ycor() - 5 * k)
    goto(xcor() + 15 * k, ycor() + 8 * k)
    goto(xcor() + 0 * k, ycor() + 1 * k)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')


update()
exitonclick()
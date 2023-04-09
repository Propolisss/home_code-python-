from turtle import *
tracer(0)
screensize(10000, 10000)
k = 20
left(90)

for i in range(5):
    goto(xcor() + 5 * k, ycor() + 4 * k)
    goto(xcor() + 4 * k, ycor() - 4 * k)
    goto(xcor() - 7 * k, ycor() - 2 * k)
    goto(xcor() - 2 * k, ycor() + 2 * k)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')


update()
exitonclick()
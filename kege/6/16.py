from turtle import *
k = 20
tracer(0)
screensize(10000, 10000)
left(0)

for i in range(2):
    goto(xcor() + 6 * k, ycor() + 2 * k)
    goto(xcor() + 0 * k, ycor() - 2 * k)

for i in range(3):
    goto(xcor() + 2 * k, ycor() - 1 * k)
    goto(xcor() - 2 * k, ycor() - 1 * k)

for i in range(6):
    goto(xcor() - 2 * k, ycor() + 1 * k)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')

update()
exitonclick()
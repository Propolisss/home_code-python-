from turtle import *
tracer(0)
screensize(10000, 10000)
k = 20
left(90)

for i in range(10):
    goto(xcor() + 4 * k, ycor() + 3 * k)
    goto(xcor() - 4 * k, ycor() + 10 * k)
    goto(xcor() + 18 * k, ycor() - 12 * k)
    goto(xcor() - 24 * k, ycor() - 12 * k)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')

update()
exitonclick()
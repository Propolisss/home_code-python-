from turtle import *
tracer(0)
k = 20
screensize(10000, 10000)
left(90)

for i in range(5):
    goto(xcor() + 6 * k, ycor() + 8 * k)
    goto(xcor() - 8 * k, ycor() + 4 * k)
    goto(xcor() + 2 * k, ycor() - 12 * k)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')

update()
exitonclick()
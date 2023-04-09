from turtle import *
tracer(0)
screensize(10000, 10000)
k = 20
left(90)

for i in range(7):
    goto(xcor() + 6 * k, ycor() - 9 * k)
    goto(xcor() - 6 * k, ycor() + 2 * k)
    goto(xcor() + 12 * k, ycor() + 3 * k)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')



update()
exitonclick()
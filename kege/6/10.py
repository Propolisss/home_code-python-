from turtle import *
k = 40
screensize(10000, 10000)
tracer(0)
left(90)

for i in range(15):
    goto(xcor() + 10 * k, ycor() + 10 * k)
    goto(xcor() + 3 * k, ycor() - 6 * k)
    goto(xcor() - 9 * k, ycor() + 3 * k)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')



update()
exitonclick()
import turtle
from turtle import *

tracer(0)
k = 40
setx(0)
sety(0)

goto(xcor() + (3 * k), ycor() + (4 * k))
dot(5, "red")
goto(xcor() - (3 * k), ycor() + (4 * k))
dot(5, "red")
goto(xcor() - (3 * k), ycor() - (4 * k))
dot(5, "red")
goto(xcor() + (3 * k), ycor() - (4 * k))
dot(5, "red")

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, "black")

update()
exitonclick()
from turtle import *
screensize(10000, 10000)
tracer(0)
k = 3
goto(0, 0)

for i in range(1):
    goto(xcor() * k + 15 * k, ycor() * k + 8 * k)
    dot(5, 'blue')
    goto(xcor() * k + 0, ycor() * k - 2 * k)
    dot(5, 'blue')
    goto(xcor() * k - 5 * k, ycor() * k - 12 * k)
    dot(5, 'blue')
    goto(xcor() * k - 2 * k, ycor() * k + 0)
    dot(5, 'blue')
    goto(xcor() * k - 8 * k, ycor() * k + 6 * k)
    dot(5, 'blue')




update()
exitonclick()
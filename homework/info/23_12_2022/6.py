from turtle import *
tracer(0)
screensize(10000, 10000)
k = 20
left(90)

for i in range(70):
    fd(8 * k)
    right(30)

update()
exitonclick()
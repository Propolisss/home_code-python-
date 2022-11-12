from turtle import *
tracer(0)
left(90)
k = 20

for i in range(5):
    for j in range(3):
        fd(4 * k)
        left(90)
    fd(2 * k)

update()
exitonclick()
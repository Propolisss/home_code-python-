from turtle import *
tracer(0)
screensize(10000, 10000)
left(90)
k = 20

fd(9 * k)
rt(90)

for i in range(2):
    fd(3 * k)
    rt(90)
    fd(3 * k)
    rt(270)

for i in range(2):
    fd(3 * k)
    rt(90)
fd(9 * k)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')


update()
exitonclick()
from turtle import *
tracer(0)
k = 20
screensize(10000, 10000)

for i in range(14):
    for j in range(3):
        fd(3 * k)
        rt(90)
    lt(180)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')

update()
exitonclick()
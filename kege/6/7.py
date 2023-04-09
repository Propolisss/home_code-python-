from turtle import *
tracer(0)
screensize(10000, 10000)
k = 20
left(90)

for i in range(15):
    fd(7 * k)
    rt(30)
    fd(8 * k)
    rt(150)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')

update()
exitonclick()
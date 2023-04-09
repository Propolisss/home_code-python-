from turtle import *
tracer(0)
k = 20
screensize(10000, 10000)
left(90)

for i in range(8):
    for j in range(4):
        fd(5 * k)
        rt(30)
        fd(6 * k)
        rt(150)
    rt(60)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')




update()
exitonclick()
from turtle import *
tracer(0)
screensize(10000, 10000)
k = 20
left(90)

for i in range(10):
    fd(10 * k)
    for j in range(2):
        fd(10 * k)
        right(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, "red")



update()
exitonclick()
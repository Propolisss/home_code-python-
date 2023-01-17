from turtle import *
tracer(9)
screensize(10000, 10000)
k = 20
left(90)

for i in range(5):
    for j in range(3):
        fd(2 * k)
        left(90)
    fd(4 * k)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'blue')



update()
exitonclick()
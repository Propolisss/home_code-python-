from turtle import *
tracer(0)
screensize(10000, 10000)

for i in range(15):
    goto(xcor() + 10 * 30, ycor() + 10 * 30)
    goto(xcor() + 3 * 30, ycor() - 6 * 30)
    goto(xcor() - 9 * 30, ycor() + 3 * 30)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * 30, y * 30)
        dot(5, "blue")
update()

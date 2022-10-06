from turtle import *
screensize(10000, 10000)
tracer(0)

r = 20


for i in range(2):
    goto(xcor() + 3 * r, ycor() + 4 * r)
    dot(5, "blue")
    goto(xcor() - 3 * r, ycor() + 4 * r)
    dot(5, "blue")
    goto(xcor() - 3 * r, ycor() - 4 * r)
    dot(5, "blue")
    goto(xcor() + 3 * r, ycor() - 4 * r)
    dot(5, "blue")

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * r, y * r)
        dot(4, "red")
update()

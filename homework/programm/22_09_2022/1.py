from turtle import *
tracer(0)
k = 20
for i in range(2):
    goto(xcor() + 3 * k, ycor() + 4 * k)
    dot(3, "red")
    goto(xcor() - 3 * k, ycor() + 4 * k)
    dot(3, "red")
    goto(xcor() - 3 * k, ycor() - 4 * k)
    dot(3, "red")
    goto(xcor() + 3 * k, ycor() - 4 * k)
    dot(3, "red")

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, "blue")
update()

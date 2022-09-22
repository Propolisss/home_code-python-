from turtle import *
tracer(0)
k = 20
left(90)
for i in range(9):
    fd(3 * k)
    right(45)
    fd(3 * k)
    left(90)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, "blue")
update()

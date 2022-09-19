from turtle import *
left(90)

for i in range(15):
    forward(4 * 30)
    right(60)

up()
for x in range(1, 10):
    for y in range(1, 10):
        goto(x * 30, y * 30)
        dot(5, "blue")
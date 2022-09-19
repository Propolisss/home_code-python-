from turtle import *

for i in range(7):
    fd(10 * 30)
    right(120)

up()

for x in range(12):
    for y in range(-10, 5):
        goto(x * 30, y * 30)
        dot(5, "blue")

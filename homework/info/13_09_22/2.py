from turtle import *

for i in range(6):
    left(120)
    forward(6 * 50)

up()
for i in range(-7, 100):
    for j in range(-7, 10):
        goto(i * 50, j * 50)
        dot(5, "red")
from turtle import *

for i in range(3):
    forward(8 * 50)
    left(120)

up()
for i in range(20):
    for j in range(20):
        goto(i * 50, j * 50)
        dot(5, "red")

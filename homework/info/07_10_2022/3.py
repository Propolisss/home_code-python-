from turtle import *

screensize(10000, 10000)
tracer(0)

left(90)

for i in range(4):
    for j in range(4):
        for k in range(4):
            forward(3 * 30)
            right(120)
        forward(3 * 30)
    forward(3 * 30)
update()


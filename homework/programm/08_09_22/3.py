from turtle import *
left(90)

for i in range(10):
    left(60)
    forward(300)
    left(60)
pu()
for x in range(301):
    for y in range(301):
        goto(x, y)
        dot(5)
done()
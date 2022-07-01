import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
l = []

while a + c < b:
    num = math.ceil(a / d) * d + c
    l.append(num)
    a += d + c

print(' '.join(str(i) for i in l))

import math
n = -1
k = 0
sum = 0
o = 0

while n != 0:
    n = int(input())
    if n != 0:
        k += 1
        sum += n
        o += n ** 2
s = sum ** 2 / k
ot = math.sqrt((o - s) / (k - 1))

print(ot)

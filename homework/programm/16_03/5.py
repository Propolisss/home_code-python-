maxx = 0

for i in range(10000):
    x = i
    a = 18; b = 432
    while x > 0:
        a += 1
        if x % 2 == 1:
            b -= x % 100
        x //= 10
    if a == 22 and b == 246:
        if i > maxx:
            maxx = i
print(maxx)
count = 0
x = 0
maxx = 0

for i in range(156519521, 156519521 + 1000):
    x = i
    n = 1289
    while (x+n)//1000 < 156725:
        x = x - 3
        n = n + 8
    if n//1000 == 327:
        count += 1
        if i > maxx:
            maxx = i
print(count)
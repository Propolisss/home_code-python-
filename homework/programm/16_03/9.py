maxx = 0

for i in range(10000):
    s = i
    n = 200
    while s // n >= 2:
        s = s + 5
        n = n + 5
    if 100 <= s <= 999:
        if i > maxx:
            maxx = i
print(maxx)
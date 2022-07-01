for i in range(1, 100000):
    d = i
    n = 8
    s = 78
    while s <= 1200:
        s = s + d
        n = n + 2
    if n == 46:
        maxx = i
print(maxx)
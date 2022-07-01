minn = 10000
maxx = 0
s = 0

for i in range(1000):
    s =  i
    n = 11
    while s > -9:
        s = s - 4
        n = n + 5
    if n == 56:
        if n < minn:
            minn = i
        if n > maxx:
            maxx = i
print(minn, maxx, sep = '')
minn = 1000000
maxx = 0
s = 0
n = 600
summ = 0

while summ != 100000:
    summ += 1
    s = summ
    n = 600
    while n > s:
        s = s + 3
        n = n - 6
    if n == 210:
        if n > maxx:
            maxx = summ
        if n < minn:
            minn = summ
print(maxx, minn, sep = '')
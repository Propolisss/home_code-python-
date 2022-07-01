count = 0
n = 0
minn = 10000000
num = 0
d = 0
d2 = 0

for i in range(50001,90000 + 1):
    num = i
    count = 0
    d = 2
    d2 = 0
    while d ** 2 <= i:
        if i % d == 0:
            if d2 == d:
                d2 = d
                i //= d
            else:
                d2 = d
                count += 1
                i //= d
        else:
            d += 1
    if i > 1:
        if i == d:
            count += 0
        else:
            count += 1
        if count == 3:
            n += 1
            if num < minn:
                minn = num
            #print(num)
print(n, minn, sep = ' ')
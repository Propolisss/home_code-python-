count = 0
minn = 100000
d = 0

for i in range(11000, 22001):
    d =  0
    for j in range(1, 20):
        if i % j == 0:
            if j == 11 or j == 13 or j == 17 or j == 19:
                d += 1
    if d == 2:
        count += 1
        if i < minn:
            minn = i
print(count, minn, sep = '')
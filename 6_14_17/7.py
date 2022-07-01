count = 0
n = 0
minn = 10000000

for i in range(10001,50000 + 1):
    count = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            count += 2
        if count > 17:
            n += 1
            if i < minn:
                minn = i
            break
print(n, minn, sep = '')
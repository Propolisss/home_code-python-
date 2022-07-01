count = 0
minn = 100000000000000

for i in range(2 * 10**10, (4 * 10**10) + 1, 100000):
    if i % 7 == 0 and i % 100000 == 0 and i % 13 != 0 and i % 29 != 0 and i % 43 != 0 and i % 101 != 0:
        count += 1
        if i < minn:
            minn = i
print(count, minn, sep = '')
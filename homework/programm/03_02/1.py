count = 0

for i in range(1, 1000):
    x = i
    s = 12 * (x // 10)
    n = 1
    while s < 300:
        s = s + 25
        n = n * 2
    if n > 500:
        count += 1
print(count)
count = 0

for i in range(1, 61):
    d = i
    n = 20
    s = 40
    while s + n < d:
        s = s - 10
        n = n - 20
    if n >= 0:
        count += 1
print(count)
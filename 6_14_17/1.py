count = 0
s = 0

for i in range(1000):
    s = i
    n = 10
    while s - n < 1000:
        s = s + n
        n = n + 5
    if n == 80:
        count += 1
print(count)
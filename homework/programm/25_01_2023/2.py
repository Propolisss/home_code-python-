file = open('27B.txt')
n = int(file.readline())

b50000 = [0] * 80
m50000 = [0] * 80
count = 0

for i in range(n):
    x = int(file.readline())
    ost = 0 if x % 80 == 0 else 80 - x % 80
    if x > 50000:
        count += b50000[ost] + m50000[ost]
    else:
        count += b50000[ost]

    if x > 50000:
        b50000[x % 80] += 1
    else:
        m50000[x % 80] += 1
print(count)
file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
b = [0] * 80
m = [0] * 80
count = 0

for i in nums:
    ost = 0 if i % 80 == 0 else 80 - i % 80
    if i > 50000: count += b[ost] + m[ost]
    else: count += b[ost]

    if i > 50000: b[i % 80] += 1
    else: m[i % 80] += 1
print(count)
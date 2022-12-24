file = open('27B.txt')
n = int(file.readline())
buffer = [int(file.readline()) for _ in range(4)]
nums = [int(file.readline()) for _ in range(n - 4)]
k13_1 = 0
k13_0 = 0
k1 = 0
k0 = 0
count = 0

for i in nums:
    if (i % 13 == 0) and (i & 1): count += k0
    elif (i % 13 == 0) and (i % 2 == 0): count += k1
    elif (i & 1): count += k13_0
    else: count += k13_1

    if (buffer[0] % 13 == 0) and (buffer[0] & 1): k13_1 += 1
    if (buffer[0] % 13 == 0) and (buffer[0] % 2 == 0): k13_0 += 1
    if (buffer[0] & 1): k1 += 1
    if (buffer[0] % 2 == 0): k0 += 1

    buffer.append(i)
    buffer.pop(0)
print(count)
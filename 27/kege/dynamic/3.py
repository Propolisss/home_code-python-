file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k5_1 = 0
k5_0 = 0
k1 = 0
k0 = 0
count = 0

for i in nums:
    if (i % 5 == 0) and (i & 1): count += k0
    elif (i % 5 == 0) and (i % 2 == 0): count += k1
    elif (i & 1): count += k5_0
    else: count += k5_1

    if (i % 5 == 0) and (i & 1): k5_1 += 1
    if (i % 5 == 0) and (i % 2 == 0): k5_0 += 1
    if (i & 1): k1 += 1
    if (i % 2 == 0): k0 += 1
print(count)

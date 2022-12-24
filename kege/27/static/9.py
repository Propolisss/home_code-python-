file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
ns = [0] * 2001

for i in nums:
    if 0 <= i <= 2000:
        ns[i] += 1

count = (ns[0] * ns[2000]) + (ns[2000] * (ns[2000] - 1) // 2) + (ns[1000] * (ns[1000] - 1) // 2)

for i in range(1, len(ns) // 2):
    count += ns[i] * ns[2000 - i]
print(count)


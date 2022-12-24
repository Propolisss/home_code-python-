file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = [0] * 131
count = 0

for i in nums:
    ost = 0 if i % 131 == 0 else 131 - (i % 131)
    count += k[ost]

    k[i % 131] += 1
print(count)
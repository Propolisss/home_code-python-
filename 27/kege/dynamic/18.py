file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = [0] * 135
count = 0

for i in nums:
    if i <= 134:
        for j in range(i + 1, 134 + 1):
            if (i + j) <= 134:
                count += k[j]
        k[i] += 1
print(count)
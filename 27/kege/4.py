file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k = [0] * 131

for i in range(n):
    k[nums[i] % 131] += 1

summ = k[0] * (k[0] - 1) // 2

for i in range(1, len(k) // 2 + 1):
    summ += k[i] * k[131 - i]
print(summ)
file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]

k7 = k = 0

for i in range(n):
    if nums[i] % 7 == 0:
        k7 += 1
    else:
        k += 1
print(k7 * (k7 - 1) // 2 + k7 * k)
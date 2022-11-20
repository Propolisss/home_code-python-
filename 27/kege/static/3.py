file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k65 = k13 = k5 = k = 0

for i in range(n):
    if nums[i] % 65 == 0:
        k65 += 1
    elif nums[i] % 13 == 0:
        k13 += 1
    elif nums[i] % 5 == 0:
        k5 += 1
    else:
        k += 1
print(k65 * (k65 - 1) // 2 + k65 * (k + k5 + k13) + k13 * k5)
file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k5_1 = k5_0 = k1 = k0 = 0

for i in range(n):
    if nums[i] % 5 == 0 and nums[i] % 2 == 0:
        k5_0 += 1
    elif nums[i] % 5 == 0 and nums[i] % 2 != 0:
        k5_1 += 1
    elif nums[i] & 1:
        k1 += 1
    else:
        k0 += 1
print(k5_1 * k5_0 + k5_1 * k0 + k5_0 * k1)
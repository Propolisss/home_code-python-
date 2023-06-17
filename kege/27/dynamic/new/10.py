file = open('27B_2751.txt')
n = int(file.readline())
nums = [int(i) for i in file]
count = 0
k13_1 = k13_0 = k1 = k0 = 0

for i in range(4, n):
    x = nums[i]
    if x % 13 == 0 and x % 2 == 0: count += k1
    if x % 13 == 0 and x % 2 != 0: count += k0
    if x % 13 != 0 and x % 2 == 0: count += k13_1
    if x % 13 != 0 and x % 2 != 0: count += k13_0

    if nums[i - 4] % 13 == 0 and nums[i - 4] % 2 == 0: k13_0 += 1
    if nums[i - 4] % 13 == 0 and nums[i - 4] % 2 != 0: k13_1 += 1
    if nums[i - 4] % 2 != 0: k1 += 1
    if nums[i - 4] % 2 == 0: k0 += 1
print(count)
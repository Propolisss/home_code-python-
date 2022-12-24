file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k1 = k0 = 0

for i in range(n):
    if nums[i] & 1:
        k1 += 1
    else:
        k0 += 1
print(k1 * (k1 - 1) // 2 + k0 * (k0 - 1) // 2)
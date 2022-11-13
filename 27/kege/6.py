file = open('27B (1).txt')
n = int(file.readline())
nums = [int(i) for i in file]

k1 = []
k0 = []

for i in range(n):
    if nums[i] & 1:
        k1.append(nums[i])
    else:
        k0.append(nums[i])

print(max(k1) + max(k0))


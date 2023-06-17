file = open('27B_2764.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k6 = [float('inf')] * 23
k3 = [float('inf')] * 23
k2 = [float('inf')] * 23
k = [float('inf')] * 23
minn = float('inf')

for i in range(6, n):
    x = nums[i]
    ost = (23 - x % 23) % 23
    if x % 6 == 0:
        minn = min(minn, x + k[ost])
    elif x % 3 == 0:
        minn = min(minn, x + k2[ost])
    elif x % 2 == 0:
        minn = min(minn, x + k3[ost])
    else:
        minn = min(minn, x + k6[ost])

    if nums[i - 6] % 6 == 0:
        k6[nums[i - 6] % 23] = min(k6[nums[i - 6] % 23], nums[i - 6])
    if nums[i - 6] % 3 == 0:
        k3[nums[i - 6] % 23] = min(k3[nums[i - 6] % 23], nums[i - 6])
    if nums[i - 6] % 2 == 0:
        k2[nums[i - 6] % 23] = min(k2[nums[i - 6] % 23], nums[i - 6])
    k[nums[i - 6] % 23] = min(k[nums[i - 6] % 23], nums[i - 6])
print(minn)
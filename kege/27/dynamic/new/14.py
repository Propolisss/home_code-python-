file = open('27B_2755.txt')
n = int(file.readline())
nums = [int(i) for i in file]
minn = float('inf')
k = [float('inf')] * 144

for i in range(n):
    ost = (144 - nums[i] % 144) % 144
    if k[ost] < nums[i]:
        minn = min(minn, k[ost] + nums[i])

    k[nums[i] % 144] = min(k[nums[i] % 144], nums[i])
print(minn)
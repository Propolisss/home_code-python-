file = open('27B.txt')
n = int(file.readline())
nums = [int(i) for i in file]

k31 = []
k = []

for i in range(n):
    if nums[i] % 31 == 0:
        k31.append(nums[i])
    else:
        k.append(nums[i])
k31.sort()
k.sort()
ans = k31[:2] + k[:2]
minn = float('inf')
for i in range(len(ans)):
    for j in range(i + 1, len(ans)):
        if ans[i] * ans[j] % 31 == 0:
            minn = min(ans[i] * ans[j], minn)
print(minn)
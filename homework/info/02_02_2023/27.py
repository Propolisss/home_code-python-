from math import ceil

file = open('27B')
n = int(file.readline())
nums = [[int(j) for j in i.split()] for i in file]
pref = [0] * n
minn = float('inf')

for i in range(n):
    pref[i] = pref[i - 1] + ceil(nums[i][1] / 36)

summ = 0
for i in range(1, n):
    summ += abs(nums[i][0] - nums[0][0]) * ceil(nums[i][1] / 36)

minn = summ
for i in range(1, n):
    summ = summ + (pref[i - 1] * abs(nums[i][0] - nums[i - 1][0])) - ((pref[-1] - pref[i - 1]) * abs(nums[i][0] - nums[i - 1][0]))
    minn = min(minn, summ)
print(minn)
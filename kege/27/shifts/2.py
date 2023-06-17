file = open('27B_6320.txt')
n, m = map(int, file.readline().split())
nums = [int(i) for i in file]
nums *= 3
summ = sum(nums[:2 * m + 1])
maxx = summ

for i in range(m + 1, 2 * n - m):
    summ += nums[i + m] - nums[i - (m + 1)]
    maxx = max(maxx, summ)
print(maxx)
file = open('27B_4630.txt')
n, k, m = map(int, file.readline().split())
nums = [0] * (k + 1)

for i in range(n):
    km, c = map(int, file.readline().split())
    p = c // 9 if c % 9 == 0 else c // 9 + 1
    nums[km] = p
summ = sum(nums[:2 * m + 1])
nums *= 3


maxx = summ

for i in range(m + 1, len(nums) - m):
    summ += nums[i + m] - nums[i - m - 1]
    if nums[i] > 0:
        maxx = max(maxx, summ)
print(maxx)
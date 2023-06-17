file = open('27A_6321.txt')
n, v, m = map(int, file.readline().split())
nums = [0] * 5_000_000
for i in file:
    nn = [int(j) for j in i.split()]
    c = nn[1] // v if nn[1] % v == 0 else nn[1] // v + 1
    nums[nn[0]] = c

summ = sum(nums[:2 * m + 1])
maxx = summ

for i in range(m + 1, len(nums) - m):
    summ += nums[i + m] - nums[i - m - 1]
    if nums[i]:
        maxx = max(maxx, summ)
print(maxx)
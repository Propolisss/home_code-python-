file = open('27B_5919.txt')
n, k, v = map(int, file.readline().split())
nums = [0] * k
all_sum = 0
for i in range(n):
    km, c = map(int, file.readline().split())
    p = c // v if c % v == 0 else c // v + 1
    nums[km % k] = p
    all_sum += p
nums *= 3
summ = 0

for i in range(k):
    summ += min(i, k - i) * nums[i]
minn = float('inf')
if nums[0]: minn = summ
chep = sum(nums[1 : k // 2 + 1])

for i in range(1, k):
    summ += (all_sum - chep) - chep
    chep += nums[k // 2 + i] - nums[i]
    if nums[i]:
        minn = min(minn, summ)
print(minn)
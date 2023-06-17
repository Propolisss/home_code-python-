file = open('27_A_3587.txt')
n = int(file.readline())
nums = [int(i) for i in file]
all_sum = sum(nums)
nums *= 2
summ = 0

for i in range(n):
    summ += min(i, n - i) * nums[i]
minn = summ
minn_id = 0
chep = sum(nums[1 : n // 2 + 1])

for i in range(1, n):
    summ += (all_sum - chep) - chep
    if summ < minn:
        minn = summ
        minn_id = i
    chep += - nums[i] + nums[n // 2 + i]
print(minn_id + 1)
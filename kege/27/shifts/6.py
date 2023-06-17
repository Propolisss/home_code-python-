file = open('27A_5644.txt')
n = int(file.readline())
nums = [int(i) for i in file]
all_summ = sum(nums)
summ = 0

for i in range(n):
    summ += nums[i] * i

maxx = summ
prev = 0
for i in range(1, n):
    prev += nums[i - 1]
    summ += prev - (all_summ - prev)
    maxx = max(maxx, summ)
print(maxx)
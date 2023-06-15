file = open('26_1395.txt')
s, n = map(int, file.readline().split())
nums = sorted(int(i) for i in file)
summ = 0
count = 0

for i in range(len(nums)):
    if summ + nums[i] <= s:
        summ += nums[i]
        count += 1
print(n - count, sum(nums) - summ)
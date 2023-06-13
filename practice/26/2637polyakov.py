file = open('26-20.txt')
s, n = map(int, file.readline().split())
nums = [int(i) for i in file]
nums.sort()
count = 0
summ = 0
last = float('-inf')
flags = [0] * n

for i in range(len(nums)):
    if summ + nums[i] <= s:
        summ += nums[i]
        count += 1
        last = nums[i]
        flags[i] = 1

for i in range(n - 1, -1, -1):
    if not(flags[i]):
        if summ - last + nums[i] <= s:
            print(count, nums[i])
            break
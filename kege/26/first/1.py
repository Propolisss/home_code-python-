file = open('26_225.txt')
s, n = map(int, file.readline().split())
nums = sorted([int(i) for i in file])
summ = 0
minn = float('inf')
count = 0

for i in range(n - 1, -1, -1):
    if nums[i] + summ <= s:
        summ += nums[i]
        minn = min(minn, nums[i])
        count += 1

print(count, minn)
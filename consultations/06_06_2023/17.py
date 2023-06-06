nums = [int(i) for i in open('17-345.txt')]
minn = min(i for i in nums if i % 100 == 52)
maxx = max(i for i in nums if i % 100 == 52)
ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] < (maxx - minn)) ^ (nums[i] < (maxx - minn)):
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))
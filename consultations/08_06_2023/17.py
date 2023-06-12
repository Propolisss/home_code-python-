nums = [int(i) for i in open('17-344.txt')]
minn = min(i for i in nums if i % 103 == 0)
ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] + nums[i]) % 2 == 0 and abs(nums[i - 1] - nums[i]) % minn == 0:
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))
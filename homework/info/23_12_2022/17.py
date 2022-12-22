nums = [int(i) for i in open('17 (4).txt')]

minn = min(nums)
ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] % 117 == minn) or (nums[i] % 117 == minn):
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))
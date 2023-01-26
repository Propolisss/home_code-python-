nums = [int(i) for i in open('17 (3).txt')]
sr = sum(nums) / len(nums)
ans = []
count = 0

for i in range(2, len(nums) - 1):
    if (nums[i] * nums[i - 1]) > (nums[i - 2] * nums[i + 1]):
        ans.append(nums[i] + nums[i - 1])
        if nums[i] > sr or nums[i - 1] > sr:
            count += 1
print(max(ans), count)
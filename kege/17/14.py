nums = [int(i) for i in open('17_2238.txt')]
avg = sum(nums) / len(nums)
ans = []

for i in range(2, len(nums)):
    if (nums[i - 2] > avg) + (nums[i - 1] > avg) + (nums[i] > avg) >= 2:
        ans.append(nums[i - 2] + nums[i - 1] + nums[i])
print(len(ans), max(ans))
n = int(input())
nums = [int(i) for i in input().split()]
count = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        count += abs(nums[i] - nums[i - 1])
        nums[i] += abs(nums[i] - nums[i - 1])
print(count)
nums = [int(i) for i in input().split()]

for i in range(len(nums)):
    if nums.count(nums[i]) == 1:
        print(nums[i])
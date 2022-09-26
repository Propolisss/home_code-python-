nums = [int(i) for i in input().split()]

nums[nums.index(max(nums))], nums[nums.index(min(nums))] = nums[nums.index(min(nums))], nums[nums.index(max(nums))]
print(*nums)
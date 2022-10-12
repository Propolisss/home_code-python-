n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

del nums[nums.index(max(nums))]
del nums[nums.index(min(nums))]

print(*nums, sep='\n')
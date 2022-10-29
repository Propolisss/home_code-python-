nums = [int(i) for i in input().split()]

maxx = max(nums)
minn = min(nums)
maxx_index = nums.index(maxx)
minn_index = nums.index(minn)

nums[maxx_index], nums[minn_index] = minn, maxx
print(*nums)
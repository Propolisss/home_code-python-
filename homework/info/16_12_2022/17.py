nums = [int(i) for i in open('17 (4).txt')]

maxx_diff = float('-inf')
count = 0
for i in range(len(nums)):
    if i == 0:
        if nums[i] < nums[i + 1]:
            count += 1
            maxx_diff = max(maxx_diff, abs(nums[i + 1] - nums[i]))
    elif i == len(nums) - 1:
        if nums[i] < nums[i - 1]:
            count += 1
            maxx_diff = max(maxx_diff, abs(nums[i - 1] - nums[i]))
    else:
        if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
            count += 1
            maxx_diff = max(maxx_diff, abs(nums[i + 1] - nums[i]))
            maxx_diff = max(maxx_diff, abs(nums[i - 1] - nums[i]))
print(count, maxx_diff)
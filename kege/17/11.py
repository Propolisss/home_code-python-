nums = [int(i) for i in open('17_2002.txt')]
ans = []

for i in range(3, len(nums)):
    if nums[i - 3]  > nums[i - 2] > nums[i - 1] > nums[i] and (nums[i - 3] - nums[i]) > 1000:
        ans.append(nums[i - 3] + nums[i - 2] + nums[i - 1] + nums[i])
print(len(ans), min(ans))
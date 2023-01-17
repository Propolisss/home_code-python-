nums = [int(i) for i in open('17 (4).txt')]

sr = (max(nums) + min(nums)) / 2
ans = []

for i in range(len(nums) // 2 + 1):
    if (sr > nums[i] and sr < nums[-i - 1]) or (sr < nums[i] and sr > nums[-i - 1]):
        ans.append(nums[i] + nums[-i - 1])
print(len(ans), max(ans))
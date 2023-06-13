nums = [int(i) for i in open('17_1999.txt')]
ans = []

for i in range(2, len(nums)):
    if (nums[i - 2] % 12 == 0 or nums[i - 1] % 12 == 0 or nums[i] % 12 == 0) and (nums[i - 2] % 3 == 0 and nums[i - 1] % 3 == 0 and nums[i] % 3 == 0):
        ans.append((nums[i - 2] + nums[i - 1] + nums[i]) / 3)
print(len(ans), min(ans))
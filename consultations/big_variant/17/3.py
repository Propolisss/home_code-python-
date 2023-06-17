from math import gcd

nums = [int(i) for i in open('17_6059.txt')]
ans = []

for i in range(1, len(nums)):
    if gcd(nums[i - 1], nums[i]) > 100 and nums[i - 1] % 2 == 0 and nums[i] % 2 == 0 and (nums[i - 1] != 0 and nums[i] != 0):
        ans.append(abs(nums[i - 1] - nums[i]))
print(len(ans), max(ans))
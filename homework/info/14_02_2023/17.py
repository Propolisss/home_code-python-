nums = [int(i) for i in open('17 (3).txt')]
maxx = float('-inf')

for i in nums:
    if (i ** 0.5).is_integer():
        maxx = max(maxx, i)


ans = []

for i in range(1, len(nums)):
    if ((nums[i - 1] * nums[i]) ** 0.5).is_integer() and ((nums[i - 1] <= 3 * maxx) or (nums[i] <= 3 * maxx)):
        ans.append((nums[i - 1] * nums[i]) ** 0.5)
print(len(ans), max(ans) + min(ans))
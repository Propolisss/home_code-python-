nums = [int(i) for i in open('17')]
maxx = float('-inf')

for i in nums:
    if i % 3 == 0:
        maxx = max(maxx, i)

ans = []

for i in range(1, len(nums)):
    if ((str(nums[i])[-1] == '3') ^ (str(nums[i - 1])[-1] == '3')) and (nums[i] ** 2 + nums[i - 1] ** 2) >= (maxx ** 2):
        ans.append(nums[i] ** 2 + nums[i - 1] ** 2)
print(len(ans), max(ans))
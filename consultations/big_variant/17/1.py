nums = [int(i) for i in open('17_8504.txt')]
minn = min(i for i in nums if 100 <= i <= 999 and i % 10 == 5)
ans = []

for i in range(1, len(nums)):
    if ((100 <= nums[i - 1] <= 999) or (100 <= nums[i] <= 999)) and (nums[i - 1] + nums[i]) % minn == 0:
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))
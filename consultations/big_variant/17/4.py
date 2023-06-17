nums = [int(i) for i in open('17_4542.txt')]
minn = min(i for i in nums if i % 37 == 0)
maxx = max(i for i in nums if i % 73 == 0)
ans = []
for i in range(1, len(nums)):
    if (maxx < nums[i - 1] < minn) ^ (maxx < nums[i] < minn):
        ans.append(nums[i - 1] + nums[i])
print(len(ans), min(ans))
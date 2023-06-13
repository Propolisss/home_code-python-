nums = [int(i) for i in open('17_2239.txt')]
maxx = max(i for i in nums if i % 19 == 0)
ans = []

for i in range(1, len(nums)):
    if nums[i - 1] > maxx or nums[i] > maxx:
        ans.append(nums[i - 1] + nums[i])
print(len(ans), min(ans))
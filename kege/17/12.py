nums = [int(i) for i in open('17_2400.txt')]
ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] + nums[i]) >= 100 and (nums[i - 1] < 0 or nums[i] < 0):
        ans.append(nums[i - 1] * nums[i])
print(len(ans), max(ans))
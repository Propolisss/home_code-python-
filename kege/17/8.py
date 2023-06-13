nums = [int(i) for i in open('17_1998.txt')]
ans = []

for i in range(2, len(nums)):
    if (nums[i - 2] * nums[i - 1] * nums[i]) % 7 == 0 and abs(nums[i - 2] + nums[i - 1] + nums[i]) % 10 == 5:
        ans.append(nums[i - 2] + nums[i - 1] + nums[i])
print(len(ans), max(ans))
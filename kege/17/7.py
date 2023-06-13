nums = [int(i) for i in open('17_1994.txt')]
ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] * nums[i]) > 0 and (nums[i - 1] + nums[i]) % 7 == 0:
        ans.append(nums[i - 1] * nums[i])
print(len(ans), min(ans))
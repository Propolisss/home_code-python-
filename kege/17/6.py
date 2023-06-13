nums = [int(i) for i in open('17_1993.txt')]
ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] + nums[i]) % 3 == 0 and (nums[i - 1] + nums[i]) % 6 != 0 and abs(nums[i - 1] * nums[i]) % 10 == 8:
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))
nums = [int(i) for i in open('17_6353.txt')]
maxx = max(i for i in nums if i % 118 == 0 and i % 10 != 8)
ans = []

for i in range(2, len(nums)):
    if ((nums[i - 2] % 118 == 0) or (nums[i - 1] % 118 == 0) or (nums[i]) % 118 == 0) and ((nums[i - 2] % 1000 == 118) or (nums[i - 1] % 1000 == 118) or (nums[i]) % 1000 == 118) and (nums[i - 2] + nums[i - 1] + nums[i]) > maxx:
        ans.append(nums[i - 2] + nums[i - 1] + nums[i])
print(len(ans), max(ans) ** 2)
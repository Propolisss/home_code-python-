nums = [int(i) for i in open('17_6696.txt')]
ans = []

for i in range(2, len(nums)):
    if (nums[i - 2] >= 0 or nums[i - 1] >= 0 or nums[i] >= 0) and (nums[i - 2] + nums[i - 1] + nums[i]) % 2022 == 0:
        ans.append(nums[i - 2] + nums[i - 1] + nums[i])
print(len(ans), max(ans))
nums = [int(i) for i in open('17 (4).txt')]

ans = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if (abs(nums[i] - nums[j]) % 36 == 0) and (nums[i] % 13 == 0 or nums[j] % 13 == 0):
            ans.append(abs(nums[i] - nums[j]))
print(len(ans), max(ans))
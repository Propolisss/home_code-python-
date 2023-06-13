nums = [int(i) for i in open('17_2403.txt')]
ans = []

for i in range(1, len(nums)):
    if (nums[i - 1] % 9 == 0 and nums[i] % 9 != 0 and abs(nums[i]) % 8 == 3) or (nums[i] % 9 == 0 and abs(nums[i - 1]) % 8 == 3 and nums[i - 1] % 9 != 0):
        ans.append(max(nums[i - 1], nums[i]))
print(len(ans), max(ans))
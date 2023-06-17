nums = [int(i) for i in open('17_2398.txt')]
ans = []

for i in range(2, len(nums)):
    if not(nums[i - 2] > 0 and nums[i - 2] % 10 == 9) and (nums[i - 1] > 0 and nums[i - 1] % 10 == 9) and not(nums[i] > 0 and nums[i] % 10 == 9):
        ans.append(nums[i - 2] + nums[i - 1] + nums[i])
print(len(ans), max(ans))
nums = [int(i) for i in open('17).txt')]

ans = []

for i in range(1, len(nums)):
    if (abs(nums[i]) + abs(nums[i - 1])) > 17043 and ((abs(nums[i]) + abs(nums[i - 1])) % 3 == 0):
        ans.append(nums[i] + nums[i - 1])
print(len(ans), min(ans))
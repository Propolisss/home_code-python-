nums = [int(i) for i in open('17_2401.txt')]
ans = []

for i in range(1, len(nums)):
    if 50 <= (abs(nums[i - 1]) + abs(nums[i])) <= 200:
        ans.append(min(nums[i - 1], nums[i]))
print(len(ans), min(ans))
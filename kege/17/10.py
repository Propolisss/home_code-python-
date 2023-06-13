nums = [int(i) for i in open('17_2402.txt')]
ans = []

for i in range(2, len(nums)):
    if nums[i - 2] % 3 == 2 or nums[i - 1] % 3 == 2 or nums[i] % 3 == 2:
        ans.append(sorted([nums[i - 2], nums[i - 1], nums[i]]))
print(len(ans), sum(i[0] for i in ans))
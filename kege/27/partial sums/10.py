file = open('27B_2904.txt')
n = int(file.readline())
nums = []
ans = []

for i in range(n):
    x = int(file.readline())
    nums = [[x, 1]] + [[a + x, b + 1] for a, b in nums]
    nums = {a % 2077 : (a, b) for a, b in sorted(nums, reverse=1)}
    if 0 in nums:
        ans.append(nums[0])
    nums = list(nums.values())
print(min(ans))
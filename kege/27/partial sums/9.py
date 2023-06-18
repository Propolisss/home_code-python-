file = open('27B_1877.txt')
n = int(file.readline())
nums = [[0, 0]]
ans = []
for i in range(n):
    x = int(file.readline())
    nums = [[x, 1]] + [[a + x, b + 1] for a, b in nums]
    nums = {a % 69 : (a, b) for a, b in sorted(nums)}
    if 0 in nums:
        ans.append(nums[0])
    nums = list(nums.values())
ans.sort()
print(ans)
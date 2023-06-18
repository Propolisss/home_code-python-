file = open('27B_2256.txt')
n = int(file.readline())
nums = []
maxx = float('-inf')

for i in range(n):
    x = int(file.readline())
    nums = [[x, x % 5 == 0]] + [[a + x, b + (x % 5 == 0)] for a, b in nums]
    nums = {b % 3 : (a, b) for a, b in sorted(nums)}
    if 0 in nums:
        maxx = max(maxx, nums[0][0])
    nums = list(nums.values())
print(maxx)
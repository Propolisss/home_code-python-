file = open('27B_2900.txt')
n = int(file.readline())
nums = []
maxx = float('-inf')

for i in range(n):
    x = int(file.readline())
    nums = [x] + [a + x for a in nums]
    nums = {j % 1000 : j for j in sorted(nums)}
    if 0 in nums:
        maxx = max(maxx, nums[0])
    nums = nums.values()
print(maxx)
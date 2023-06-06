file = open('26.txt')
nums = []

for i in file:
    nums.append([int(j) for j in i.replace('A', '0').replace('B', '1').split()])
nums.sort()

maxx = float('-inf')
minn = float('inf')
flags = [0] * len(nums)
count = 0

for i in range(len(nums)):
    inner_count = 1
    curr = nums[i]
    if not flags[i]:
        for j in range(i + 1, len(nums)):
            if not flags[j]:
                if (abs(nums[j][0]) - curr[0]) >= 7 and (nums[j][1] != curr[1]):
                    inner_count += 1
                    flags[j] = 1
                    curr = nums[j]
        maxx = max(maxx, inner_count)
        count += 1
print(maxx, count)
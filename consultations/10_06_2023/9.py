file = open('9.txt')
count = 0

for i in file:
    nums = [int(j) for j in i.split()]
    nums.sort()
    if (len(nums) == len(set(nums))) ^ ((2 * (nums[0] + nums[-1])) < sum(nums[1:-1])):
        count += 1
print(count)
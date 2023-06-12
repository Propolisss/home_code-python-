file = open('9.txt')
count = 0

for i in file:
    nums = [int(j) for j in i.split()]
    if len(nums) == len(set(nums)):
        nums.sort()
        if (sum(nums) / len(nums)) >= (nums[2] + nums[3]) / 2:
            count += 1
print(count)
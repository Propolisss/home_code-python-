file = open('9_1')
count = 0

for i in file:
    nums = [int(j) for j in i.split()]
    if len(nums) == len(set(nums)):
        ch = [j for j in nums if j % 2 == 0]
        nech = [j for j in nums if j % 2 != 0]
        if len(ch) > len(nech) and sum(ch) < sum(nech):
            count += 1
print(count)
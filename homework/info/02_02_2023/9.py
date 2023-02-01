nums = [[int(j) for j in i.split()] for i in open('9.txt')]

count = 0

for i in range(len(nums)):
    rep = []
    norep = []

    for j in nums[i]:
        if nums[i].count(j) > 1:
            rep.append(j)
        else:
            norep.append(j)
    if len(rep) == 2:
        if (sum(norep) /  len(norep)) <= sum(rep):
            count += 1
print(count)
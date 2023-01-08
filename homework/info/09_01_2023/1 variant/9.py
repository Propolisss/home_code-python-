count = 0

for i in open('9 (3).csv'):
    nums = [int(s) for s in i.split(';')]
    print(nums)
    rep = []
    non_rep = []
    for j in nums:
        if nums.count(j) == 2:
            rep.append(j)
        elif nums.count(j) == 1:
            non_rep.append(j)
    if all(j >= k for j in rep for k in non_rep) and len(rep) > 0:
        count += 1
print(count)

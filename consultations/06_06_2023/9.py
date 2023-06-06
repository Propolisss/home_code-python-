file = open('9.txt')
count = 0

for i in file:
    nums = [int(j) for j in i.split()]
    rep = []
    no_rep = []
    for j in nums:
        if nums.count(j) == 1:
            no_rep.append(j)
        else:
            rep.append(j)
    if len(rep) >= 2 and sum(no_rep) % 2 != 0:
        count += 1
print(count)
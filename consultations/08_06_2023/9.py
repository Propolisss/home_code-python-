file = open('9.txt')
count = 0

for i in file:
    nums = [int(j) for j in i.split()]
    rep = [j for j in nums if nums.count(j) == 2]
    no_rep = [j for j in nums if nums.count(j) == 1]
    if len(rep) == 2 and len(no_rep) == 4:
        if max(no_rep) + min(no_rep) <= sum(rep):
            count += 1
print(count)
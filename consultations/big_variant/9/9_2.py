file = open('9_2.txt')
count = 0

for i in file:
    nums = [int(j) for j in i.split()]
    rep = []
    no_rep = []
    ch = [j for j in nums if j % 2 == 0]
    nech = [j for j in nums if j & 1]
    sr1 = sum(ch) / len(ch) if len(ch) > 0 else 0
    sr2 = sum(nech) / len(nech) if len(nech) > 0 else 0
    for i in nums:
        if nums.count(i) == 1:
            no_rep.append(i)
        elif nums.count(i) == 2:
            rep.append(i)

    if (len(rep) == 2 and len(no_rep) == 4) ^ (abs(sr1 - sr2) > 50):
        count += 1
print(count)
from math import *
file = open('27-36a.txt')
n = int(file.readline())
ost = []
summ = 0

for i in file:
    nums = [int(j) for j in i.split()]
    nums.sort()
    gs = [gcd(nums[0], nums[1]), gcd(nums[1], nums[2]), gcd(nums[0], nums[2])]
    gs.sort()
    summ += max(gs)
    ost.append(gs[-1] - gs[-2])

if summ % 10 == 0:
    print(summ)
else:
    for i in range(len(ost)):
        if (summ - ost[i]) % 10 == 0:
            print(summ - ost[i])
            break
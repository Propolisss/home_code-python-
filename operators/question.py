n = 1
s = 0
summ = 200

while n != 46:
    n = 1
    summ += 1
    s = summ
    while s > 200:
        s = s - 15
        n = n + 3
print(summ)
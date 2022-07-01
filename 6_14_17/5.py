st = ''
summ = 0

for i in range(23, 1000):
    summ = 0
    x = i
    z = 36 ** 17 - 6 ** x + 71
    while z > 0:
        summ += z % 6
        z //= 6
    if summ == 61:
        print(i)
        break
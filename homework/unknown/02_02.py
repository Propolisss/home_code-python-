z = 103 * 7 ** 103 - 5 * 7 ** 57 + 98
summ = 0

while z > 0:
    summ += z % 7
    z //= 7
print(summ)
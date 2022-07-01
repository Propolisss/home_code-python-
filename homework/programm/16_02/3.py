z = 6 ** 203 + 5 * 6 ** 405 - 3 * 6 ** 144 + 76
summ  = 0

while z > 0:
    summ += z % 6
    z //= 6
print(summ)
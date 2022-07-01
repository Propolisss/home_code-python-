z = (5 ** 300 * 15 ** 100) - (25 ** 50 + 125 ** 100)
summ = 0

while z > 0:
    if z % 5 != 4:
        summ += z % 5
    z //= 5
print(summ)
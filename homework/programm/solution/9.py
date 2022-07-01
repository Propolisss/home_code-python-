z = (66 + 6 ** 2019) * 6 ** 2019 + 66 + 6 ** 6
summ = 0

while z > 0:
    summ += z % 6
    z //= 6
print(summ)
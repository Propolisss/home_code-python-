z = (7 ** 160 * 7 ** 90) - (14 ** 150 + 2 ** 13)
summ = 0
last = 0

while z > 0:
    last = z % 7
    if last != 6:
        summ += last
    z //= 7
print(summ)
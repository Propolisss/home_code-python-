summ = 0

for x in range(158):
    n1 = 2 + x * 158 + 3 * 158 ** 2 + 7 * 158 ** 3 + 2 * 158 ** 4
    n2 = 9 * 158 + 3 * 158 ** 2 + x * 158 ** 3 + 158 ** 4
    if (n1 + n2) % 73 == 0:
        summ += ((n1 + n2) // 73)
print(summ)
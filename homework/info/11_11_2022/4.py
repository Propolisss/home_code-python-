z = 16 ** 44 * 16 ** 30 - (32 ** 5 * (8 ** 40 - 8 ** 32) * (16 ** 17 - 32 ** 4))
z = hex(z)[2:].replace('f', '0')

i = 0

while z[i] == '0':
    i += 1
print(z[i + 1 + 3:].count('0'))


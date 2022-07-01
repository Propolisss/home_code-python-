z = 9 ** 81 + 27 ** 729 - 4
count = 0

while z > 0:
    if (z % 9 == 8) or (z % 9 == 0):
        count += 1
    z //= 9
print(count)
z = 49 ** 13 + 7 ** 33 - 49
count = 0

while z > 0:
    if z % 7 == 6:
        count += 1
    z //= 7
print(count)
count = 0

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if (y < x) and (y < (55 * 2 ** 0.5 - x)) and (y > (-x)) and y > (x - 55 * 2 ** 0.5):
            count += 1
print(count)
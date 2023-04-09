count = 0

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if 0 < y < 15 and y < 3 * x and y > (x / 4 - 14):
            count += 1
print(count)
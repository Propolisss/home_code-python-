
count = 0

for x in range(1, 1000):
    for y in range(1, 1000):
        if (y < x) and (y < 200 * 2 ** 0.5) and (y < -x + 400 + 400 * 2 ** 0.5):
            count += 1
            print(count)
print(count)
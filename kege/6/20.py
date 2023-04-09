count = 0

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if y > (- 3 ** 0.5 / 3 * x) and x < 0 and y < (3 ** 0.5 / 3 * x + 30):
            count += 1
print(count)
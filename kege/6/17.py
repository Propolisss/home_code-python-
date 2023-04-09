count = 0


for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if y < 90 and y < 3 * x and y > x:
            count += 1
print(count)
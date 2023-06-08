from math import sqrt

count = 0

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if x < 0 and y > -(1 / (3 ** 0.5)) * x and y < 1 / (3 ** 0.5) * x + 30:
            count += 1
print(count)
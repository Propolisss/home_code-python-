from itertools import *

def f(x):
    b = 70 <= x <= 80
    return (x % 12 == 0) and b and (x % a != 0)

count = 0

for a in range(1, 100_000):
    if all(f(x) == 0 for x in range(1, 100_000)):
        count += 1
print(count)
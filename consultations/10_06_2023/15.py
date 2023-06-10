
def f(x):
    p = 5 <= x <= 137
    return ((x % 115 == 0) and (x % 5 != 0)) or (( (a % x == 0) <= (a % 5 != 0)) and (not(5 <= a <= 137)))

for a in range(1, 100_000):
    if any(f(x) == 1 for x in range(1, 100_000)) and any(f(x) == 0 for x in range(1, 100_000)):
        print(a)
        break
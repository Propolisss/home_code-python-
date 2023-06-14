def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

for i in range(55_000_000, 60_000_000 + 1):
    temp = i
    while temp % 2 == 0: temp //= 2
    if simple(int(temp ** 0.25)) and (temp ** 0.25).is_integer():
        print(i, temp)
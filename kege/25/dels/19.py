def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

for i in range(113_000_000, 114_000_000 + 1):
    temp = i
    if temp % 2 == 0 and temp % 4 != 0:
        temp //= 2
        if (temp ** 0.5).is_integer() and simple(int(temp ** 0.5)):
            print(i, 2 * int(temp ** 0.5))
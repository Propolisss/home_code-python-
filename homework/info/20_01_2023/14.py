def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for x in range(1, 1_000_000):
    if sum(int(i) for i in to_base(27 ** 7 - 3 ** 11 + 36 - x, 3)) == 22:
        print(x)
        break
def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for x in range(1, 100_000):
    if sum(to_base(36 ** 17 - 6 ** x + 71, 6)) == 61:
        print(x)
        break
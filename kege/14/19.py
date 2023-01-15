def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for n in range(100_000):
    if len(to_base(n, 7)) == 2 and len(to_base(n, 6)) == 3 and to_base(n, 13)[-1] == 3:
        print(n)
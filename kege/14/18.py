def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for n in range(1, 100_000):
    if len(to_base(n, 6)) == 2 and len(to_base(n, 5)) == 3 and to_base(n, 11)[-1] == 1:
        print(n)
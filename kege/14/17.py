def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for n in range(2, 1000):
    if to_base(68, n)[-1] == 2 and len(to_base(68, n)) == 4:
        print(n)
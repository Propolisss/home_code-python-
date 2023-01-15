def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for x in range(21, 29 + 1):
    if to_base(x, 3)[-2:] == [1, 1]:
        print(x)
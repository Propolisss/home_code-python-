def to_base(n, base):
    arr = []
    temp_n = n

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr


for x in range(1, 100_000):
    num = 27 ** 7 - 3 ** 11 + 36 - x
    if sum(to_base(num, 3)) == 22:
        print(x)
        break
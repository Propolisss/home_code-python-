
def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for x in range(1, 1_000_000):
    if sum(to_base(64 ** 11 - 4 ** 10 + 96 - x, 4)) == 71:
        print(x)
        break
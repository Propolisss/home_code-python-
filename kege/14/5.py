def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for x in range(1000):
    num = 125 ** 200 - 5 ** x + 74
    if to_base(num, 5).count(4) == 100:
        print(x)
        break
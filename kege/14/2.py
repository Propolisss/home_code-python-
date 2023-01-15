def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr
print(to_base(3 * 16 ** 8 - 4 ** 5 + 3, 4).count(3))
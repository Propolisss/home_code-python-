def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

print(to_base(6 * 144 ** 26 + 11 * 12 ** 75 - 48, 12).count(11))
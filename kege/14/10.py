def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

print(to_base(5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875, 6).count(5) - to_base(5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875, 6).count(0))
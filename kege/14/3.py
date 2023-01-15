def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr
print(to_base(2 * 27 ** 7 + 3 ** 10 - 9, 3).count(0))
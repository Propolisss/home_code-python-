def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr
print(sum(to_base(51 * 7 ** 12 - 7 ** 3 - 22, 7)))
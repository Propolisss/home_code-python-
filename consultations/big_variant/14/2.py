def to_base(n, base):
    arr = []
    temp_n = n

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

num = 3 * 625 ** 173 + 4 * 125 ** 180 + 3 * 25 ** 157 + 2 * 5 ** 155 + 156
print(to_base(num, 25).count(0))
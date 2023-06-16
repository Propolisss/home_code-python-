def to_base(n, base):
    arr = []
    temp_n = n

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr
n = 673 ** 7 + 67 ** 6 + 3 ** 3
print(to_base(n, 12).count(10) * 10 - to_base(n, 12).count(8) * 8)
def to_base(n, base):
    temp_n = n
    arr = ''

    while temp_n:
        arr = str(temp_n % base) + arr
        temp_n //= base
    return arr

minn = float('inf')
for i in range(1, 10_000):
    n = to_base(i, 3)
    n += str(i % 3)
    if 100 <= int(n, 3) <= 999:
        minn = min(minn, int(n, 3))
print(minn)
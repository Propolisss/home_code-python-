def to_base(n, base):
    arr = []
    temp_n = n

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr
minn = float('inf')
maxx = float('-inf')
for x in range(1, 10_000_000):
    fir = to_base(x, 9)
    if len(fir) == 3 and 3 in fir:
        sec = to_base(x * 3, 9)
        if len(sec) == 3:
            minn = min(minn, x)
            maxx = max(maxx, x)
print(to_base(minn + maxx, 9))
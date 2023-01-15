def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

count = 0

for x in range(1_000_000):
    if len(to_base(x, 5)) <= 4 and len(bin(x)[2:]) >= 5 and hex(x)[-1] == 'c':
        count += 1
print(count)
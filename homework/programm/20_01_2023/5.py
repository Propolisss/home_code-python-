def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

count = 0

for i in range(2, 1_000_000 + 1, 2):
    num = to_base(i, 5)
    if len(num) == 6 and num[0] == 3:
        count += 1
print(count)
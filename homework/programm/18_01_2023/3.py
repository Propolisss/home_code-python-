def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

count = 0
for i in range(1, 1_000_000):
    num = to_base(i, 9)
    if len(num) == 5:
        if (num[0] not in [1, 3, 5, 7, 9]) and (num[-1] not in [1, 8]) and (num.count(3) <= 1):
            count += 1
print(count)

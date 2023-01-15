def to_base(n, base):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % base}{temp_st}'
        temp_n //= base
    return temp_st

count = 0
for i in range(1, 1_000_000):
    num = to_base(i, 5)
    if len(num) == 6:
        if num[0] != '1' and num[-1] not in '34':
            count += 1
print(count)
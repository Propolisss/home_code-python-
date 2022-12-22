def f(n, base):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % base}{temp_st}'
        temp_n //= base
    return temp_st

count = 0

for i in range(1, 1_000_000):
    n = f(i, 9)
    if (len(n) == 5) and (n[0] not in '13579') and (n[-1] not in '18') and (n.count('3') <= 1):
        count += 1
print(count)
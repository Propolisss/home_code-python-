def f(n, base):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % base}{temp_st}'
        temp_n //= base
    return temp_st

for i in range(20, 30):
    if f(i, 3).endswith('11'):
        print(i)
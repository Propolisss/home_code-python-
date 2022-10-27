def to_four(n):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % 4}{temp_st}'
        temp_n //= 4
    return temp_st

s = set()

for x in range(0, 1000):
    result = 3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 4 ** x - 2022
    res = to_four(result)
    summ = sum(int(i) for i in str(res))
    s.add(summ)
print(len(s))
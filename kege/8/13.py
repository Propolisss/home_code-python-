def to_base(n, base):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % base}{temp_st}'
        temp_n //= base
    return temp_st

count = 0
for i in range(100, 999 + 1):
    num = str(i)
    if all(num[j] <= num[j + 1] for j in range(len(num) - 1)):
        count += 1
print(count)
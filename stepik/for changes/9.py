z = 7 * 729 ** 543 - 6 * 81 ** 765 - 5 * 9 ** 987 - 20

def to_nine(n):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % 9}{temp_st}'
        temp_n //= 9
    return temp_st

print(to_nine(z).count('8'))
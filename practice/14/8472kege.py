def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for x in range(1, 100):
    num1 = 3 + 2 * 100 + 100 ** 2 + x * 100 ** 4 + 10 * 100 ** 5 + 7 * 100 ** 6
    num2 = x + 4 * 100 + 6 * 100 ** 2 + 10 * 100 ** 3 + 11 * 100 ** 4 + 100 ** 5
    num3 = 12 + 2 * 100 + 100 ** 2 + 8 * 100 ** 4 + 9 * 100 ** 5 + x * 100 ** 6
    if (num1 - num2 + num3) % 21 == 0:
        print(*to_base(x, 6), sep='')
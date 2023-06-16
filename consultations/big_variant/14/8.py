def to_base(n, base):
    arr = []
    temp_n = n

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr
summ = 0

for i in range(1, 95 + 1):
    if to_base(i, 3)[-2:] == [2, 1] and to_base(i, 5)[0] == 3:
        summ += i
print(summ)
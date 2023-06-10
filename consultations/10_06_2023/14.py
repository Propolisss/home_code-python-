def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

def rev(arr, base):
    summ = 0

    for i in range(len(arr)):
        summ += arr[i] * base ** i
    return summ

for x in range(1, 100):
    n1 = rev([3, 2, 1, 0, x, 10, 7], 100)
    n2 = rev([x, 4, 6, 10, 11, 1], 100)
    n3 = rev([12, 2, 1, 0, 8, 9, x], 100)
    if (n1 - n2 + n3) % 21 == 0:
        print(x, to_base(x, 6))
def ss(arr, base):
    summ = 0
    arr = arr[::-1]
    for i in range(len(arr)):
        summ += arr[i] * base ** i
    return summ
def to_base(n, base):
    arr = []
    temp_n = n

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

for x in range(16):
    n1 = ss([11, 7, 10, x, 9], 16)
    n2 = ss([5, 4, x, 14, 13], 16)
    res = to_base(n1 + n2, 6)
    if sum(res) == 25:
        print(n1 + n2)
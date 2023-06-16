def ss(arr, base):
    summ = 0
    arr = arr[::-1]
    for i in range(len(arr)):
        summ += arr[i] * base ** i
    return summ
for x in range(98):
    n1 = ss([1, 2, x, 4, 5], 98)
    n2 = ss([1, x, 9, 8], 123)
    if (n1 + n2) % 123 == 0:
        print((n1 + n2) // 123)
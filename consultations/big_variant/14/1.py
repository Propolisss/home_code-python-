def ss(arr, base):
    summ = 0
    arr = arr[::-1]
    for i in range(len(arr)):
        summ += arr[i] * base ** i
    return summ

for x in range(15):
    n1 = ss([9, 9, 6, 5, 8, x, 2, 9], 15)
    n2 = ss([1, 0, 2, x, 0, 2, 3], 15)
    if (n1 + n2) % 14 == 0:
        print((n1 + n2) // 14)
def ss(arr, base):
    summ = 0
    arr = arr[::-1]
    for i in range(len(arr)):
        summ += arr[i] * base ** i
    return summ

for x in range(67):
    n1 = ss([3, x, 2, 1], 81)
    n2 = ss([1, 7, x, 4], 67)
    if (n1 + n2) % 35 == 0:
        print((n1 + n2) // 35)
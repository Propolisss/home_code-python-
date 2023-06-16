def ss(arr, base):
    summ = 0
    arr = arr[::-1]
    for i in range(len(arr)):
        summ += arr[i] * base ** i
    return summ

for n in range(2, 100):
    if ss([1, 0, 3], n) == ss([9, 7], n + 2):
        print(n)
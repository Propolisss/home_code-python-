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

maxx = float('-inf')
for x in range(1, 20):
    for y in range(5):
        n1 = ss([x, 1, x, 2, x, 3, x, 4], 20)
        n2 = ss([1, y, 2, y, 3, y, 4, y], 5)
        res = to_base(n1 - n2, 7)
        maxx = max(maxx, sum(res))
print(maxx)
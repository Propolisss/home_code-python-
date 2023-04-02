file = open('27B_2900.txt')

n = int(file.readline())
k = [float('inf')] * 1000
maxx = float('-inf')
summ = 0

for _ in range(n):
    x = int(file.readline())
    summ += x
    if summ % 1000 == 0:
        maxx = max(maxx, summ)

    s1 = summ - k[summ % 1000]
    maxx = max(maxx, s1)

    k[summ % 1000] = min(k[summ % 1000], summ)
print(maxx)
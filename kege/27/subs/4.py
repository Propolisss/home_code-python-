file = open('27B_2256.txt')
n = int(file.readline())
summ = 0
maxx = float('-inf')
k = [float('inf')] * 3
counter = 0

for _ in range(n):
    x = int(file.readline())
    summ += x

    if x % 5 == 0:
        counter += 1
    if counter % 3 == 0:
        maxx = max(maxx, summ)

    maxx = max(maxx, summ - k[counter % 3])
    k[counter % 3] = min(k[counter % 3], summ)
print(maxx)
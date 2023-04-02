file = open('27B_2907.txt')
n = int(file.readline())
k = [float('inf')] * 30
counter = 0
summ = 0
maxx = float('-inf')

for _ in range(n):
    x = int(file.readline())
    summ += x
    if x > 0 and (x % 2 == 0):
        counter += 1

    if counter > 0 and counter % 30 == 0:
        maxx = max(maxx, summ)

    maxx = max(maxx, summ - k[counter % 30])

    k[counter % 30] = min(k[counter % 30], summ)
print(maxx)
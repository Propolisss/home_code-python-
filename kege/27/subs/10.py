file = open('27B_2908.txt')
n = int(file.readline())
k = [float('inf')] * 7
buffer = []
summ = 0
counter = 0
maxx = float('-inf')

for _ in range(6):
    x = int(file.readline())
    summ += x
    if x > 0 and x % 7 == 0:
        counter += 1
    buffer.append([summ, counter])

for _ in range(n - 6):
    x = int(file.readline())
    summ += x

    if x > 0 and x % 7 == 0:
        counter += 1

    if counter % 7 == 0:
        maxx = max(maxx, summ)

    maxx = max(maxx, summ - k[counter % 7])

    k[buffer[0][1] % 7] = min(k[buffer[0][1] % 7], buffer[0][0])
    buffer.append([summ, counter])
    buffer.pop(0)
print(maxx)
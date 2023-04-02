file = open('27B_2363.txt')
n = int(file.readline())
buffer = []
summ = 0

for _ in range(4):
    x = int(file.readline())
    summ += x
    buffer.append(summ)

k = [0] * 117
count = 0

for _ in range(n - 4):
    x = int(file.readline())
    summ += x

    if summ % 117 == 0:
        count += 1
    count += k[summ % 117]

    k[buffer[0] % 117] += 1
    buffer.pop(0)
    buffer.append(summ)
print(count)
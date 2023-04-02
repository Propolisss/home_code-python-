file = open('27B_2901.txt')
n = int(file.readline())
summ = 0
count = 0
k = [0] * 666

for _ in range(n):
    x = int(file.readline())
    summ += x

    if summ % 666 == 0:
        count += 1

    count += k[summ % 666]
    k[summ % 666] += 1
print(count)
file = open('27B_1877.txt')
n = int(file.readline())
k = [float('inf')] * 69
lens = [0] * 69
summ = 0
minn_len = float('inf')
maxx = float('-inf')

for _ in range(n):
    x = int(file.readline())
    summ += x

    if summ % 69 == 0:
        minn_len = _ + 1
        maxx = summ

    s1 = summ - k[summ % 69]
    l1 = _ + 1 - lens[summ % 69]
    if s1 > maxx or (s1 == maxx and l1 < minn_len):
        minn_len = l1
        maxx = s1

    if summ < k[summ % 69]:
        k[summ % 69] = summ
        lens[summ % 69] = _ + 1
print(minn_len)
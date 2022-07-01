file = open('27b.txt')
n = int(file.readline())
ost = [10 ** 20] * 43
lens = [10 ** 20] * 43
minn_length = 0
summ = 0
maxx_summ = 0

for i in range(n):
    num = int(file.readline())
    summ += num
    if summ % 43 == 0:
        if summ > maxx_summ:
            maxx_summ, minn_length = summ, i + 1

    s = summ - ost[summ % 43]
    l = (i + 1) - lens[summ % 43]

    if s > maxx_summ or (s == maxx_summ and l < minn_length):
        maxx_summ, minn_length = s, l

    if summ < ost[summ % 43]:
        ost[summ % 43], lens[summ % 43] = summ, i + 1
print(minn_length)
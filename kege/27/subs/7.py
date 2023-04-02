file = open('27A_2904.txt')
n = int(file.readline())
k = [float('-inf')] * 2077
lens = [0] * 2077
summ = 0
minn = float('inf')
maxx_len = float('-inf')

for _ in range(n):
    x = int(file.readline())
    summ += x

    if summ % 2077 == 0:
        if summ < minn or (summ == minn and (_ + 1) > maxx_len):
            minn = summ
            maxx_len = _ + 1

    s1 = summ - k[summ % 2077]
    l1 = (_ + 1) - lens[summ % 2077]

    if s1 < minn or (s1 == minn and l1 > maxx_len):
        minn = s1
        maxx_len = l1

    if summ > k[summ % 2077]:
        k[summ % 2077] = summ
        lens[summ % 2077] = _ + 1
print(maxx_len)
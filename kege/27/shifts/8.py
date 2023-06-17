file = open('27B_4713.txt')
n = int(file.readline())
a = []

for i in file:
    km, c = [int(j) for j in i.split()]
    p = c // 36 if c % 36 == 0 else c // 36 + 1
    a.append([km, p])

pref = [0] * n
s = 0
for i in range(n):
    s += a[i][1]
    pref[i] = s

summ = 0
for i in range(n):
    summ += abs(a[i][0] - a[0][0]) * a[i][1]

minn = summ

for i in range(1, n):
    r = abs(a[i - 1][0] - a[i][0])
    summ += r * pref[i - 1] - r * (pref[-1] - pref[i - 1])
    minn = min(minn, summ)
print(minn)
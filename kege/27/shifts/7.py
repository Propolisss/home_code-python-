file = open('27B_6323.txt')
n, m = map(int, file.readline().split())
a = []

for i in file:
    km, c = [int(j) for j in i.split()]
    p = c // m if c % m == 0 else c // m + 1
    a.append([km, p])
pref = []
s = 0

for i in range(n):
    s += a[i][1]
    pref.append(s)
summ = 0

for i in range(n):
    summ += abs(a[i][0] - a[0][0]) * a[i][1]
minn = summ

for i in range(1, n):
    r = abs(a[i - 1][0] - a[i][0])
    summ += r * pref[i - 1] - r * (pref[-1] - pref[i - 1])
    minn = min(minn, summ)
print(minn)
n, m = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
maxx_n = 0
maxx_m = 0

for i in range(n):
    for j in range(m):
        if i == 0 and j  == 0:
            maxx = a[i][j]
        if a[i][j] > maxx:
            maxx = a[i][j]
            maxx_n = i
            maxx_m = j
print(maxx_n, maxx_m, sep = ' ')
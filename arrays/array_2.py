n = int(input())
a = [['.'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == n // 2:
            a[i][j] = '*'
        if j == n // 2:
            a[i][j] = '*'
        if i == j or (i + j) == n - 1:
            a[i][j] = '*'
for row in a:
    print(' '.join(row))
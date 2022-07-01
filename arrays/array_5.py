n = int(input())
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i + j > n - 1:
            a[i][j] = 2
        if i + j < n - 1:
            a[i][j] = 0
        elif i + j == n - 1:
            a[i][j] = 1
            
for row in a:
    print(' '.join([str(i) for i in row]))
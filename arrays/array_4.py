n  = int(input())
a = [[0] * n for i in range(n)]

for i in range(n):
    nn = n - 1
    ii = i
    for j in range(n):
        if i < j:
            a[i][j] = n - nn
            nn -= 1
        elif i > j:
            a[i][j] = ii
            ii -= 1
        else:
            a[i][j] = 0
            nn = n - 1
for row in a:
    print(' '.join([str(i) for i in row]))

#n = int(input())
#a = [[abs(i - j) for j in range(n)] for i in range(n)]
#for row in a:
#    print(' '.join([str(i) for i in row]))
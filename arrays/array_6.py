n, m = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(s) for s in input().split()]
temp = 0

def swap_columns(a, i, j):
    for k in range(n):
        for h in range(m):
            temp = a[k][h]
            if h == i:
                a[k][i] = a[k][j]
                a[k][j] = temp
                break
    for row in a:
        print(' '.join([str(i) for i in row]))
swap_columns(a, i, j)

#n, m = [int(s) for s in input().split()]
#a = [[int(j) for j in input().split()] for i in range(n)]
#i, j = [int(s) for s in input().split()]
#
#def swap_columns(a, i, j):
#    for k in range(n):
#       a[k][i], a[k][j] = a[k][j], a[k][i]
#    for row in a:
#        print(' '.join([str(i) for i in row]))
#swap_columns(a, i, j)
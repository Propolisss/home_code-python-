x = []
y = []
flag = 0

for i in range(8):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

for j in range(8):
    for k in range(j + 1, 8):
        if (abs(x[j] - x[k]) == abs(y[j] - y[k])) or (x[j] == x[k]) or (y[j] == y[k]):
            flag = 1
            break
if flag:
    print('YES')
else:
    print('NO')
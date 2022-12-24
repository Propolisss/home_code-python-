file = open('27B.txt')
n = int(file.readline())
ox = []
neox = []

for i in file:
    x, y = map(int, i.split())
    if y == 0:
        ox.append(x)
    else:
        neox.append([x, y])

ox.sort()
x1 = ox[0]
x2 = ox[-1]

maxx_y = float('-inf')
maxx_xx = float('-inf')
maxx = float('-inf')
for i in range(len(neox)):
    y3 = neox[i][1]
    x3 = neox[i][0]
    maxx = max(maxx, 0.5 * abs((x2 - x1) * (y3 - 0) - (x3 - x1) * (0 - 0)))

print(maxx)
file = open('27A.txt')
n = int(file.readline())
ox = []
oy = []
ne = []

for i in file:
    x, y = map(int, i.split())
    if x == 0:
        oy.append([x, y])
    elif y == 0:
        ox.append([x, y])
    else:
        ne.append([x, y])

print(len(ox) * len(oy) * len(ne))
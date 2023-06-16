file = open('27B_2735.txt')
n = int(file.readline())
ox = oy = o = 0

for i in range(n):
    x, y = map(int, file.readline().split())
    if x == 0:
        ox += 1
    elif y == 0:
        oy += 1
    if x != 0 and y != 0:
        o += 1
print(ox * oy * o)
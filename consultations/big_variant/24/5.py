st = open('24_3021.txt').readline()
maxx = float('-inf')

for j in 0, 1, 2:
    count = 0
    for i in range(j, len(st) - 2, 3):
        if st[i : i + 3] in ['ZXY', 'ZYX']:
            count += 1
            maxx = max(maxx, count)
        else:
            count = 0
print(maxx)
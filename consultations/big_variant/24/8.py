st = open('24_4334.txt').readline().split('A')
maxx = float('-inf')

for i in range(1, len(st) - 1 - 3):
    if (st[i] + st[i + 1] + st[i + 2] + st[i + 3]).count('R') >= 2:
        maxx = max(maxx, len((st[i] + st[i + 1] + st[i + 2] + st[i + 3])) + 3)
print(maxx)
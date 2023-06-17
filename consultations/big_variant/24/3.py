st = open('24_7016.txt').readline().replace('A', ' A ').replace('D', ' D ').split()
maxx = float('-inf')

for i in range(1, len(st) - 1):
    if ((st[i - 1] == 'A' and st[i + 1] == 'D') or (st[i - 1] == 'D' and st[i + 1] == 'A')) and st[i] not in 'AD':
        maxx = max(maxx, len(st[i]) + 2)
print(maxx)
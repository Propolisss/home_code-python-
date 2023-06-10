st = open('24_8480.txt').readline().replace('A', '*').replace('B', '*').replace('C', '*').split('**')
maxx = float('-inf')

for i in range(len(st)):
    if len(st[i]) == 0:
        continue
    if i == 0:
        maxx = max(maxx, len(st[i]) + (st[i][-1] != '*'))
    elif i == (len(st) - 1):
        maxx = max(maxx, len(st[i]) + (st[i][0] != '*'))
    else:
        maxx = max(maxx, len(st[i]) + (st[i][0] != '*') + (st[i][-1] != '*'))
print(maxx)
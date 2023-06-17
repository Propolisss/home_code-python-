st = open('24_7600.txt').readline().replace('Q', 'R').replace('S', 'R')
maxx = float('-inf')
count = 1

for i in range(len(st) - 1):
    if st[i] + st[i + 1] != 'RR':
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)
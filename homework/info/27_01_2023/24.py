st = open('24 (3).txt').readline()
maxx = float('-inf')
count = 0
i = 0

while i < len(st):
    if st[i:i + 2] == 'XY':
        count += 2
        i += 2
    elif st[i:i + 4] == 'ZZXY':
        count += 4
        i += 4
    elif st[i:i + 3] == 'ZZX':
        count += 3
        i += 3
    else:
        i += 1
        maxx = max(maxx, count)
        count = 0
maxx = max(maxx, count)


print(maxx)
st = open('24_5171.txt').readline().strip()
maxx = float('-inf')
i = 0
count = 0
while i < len(st) - 1:
    if st[i] + st[i + 1] == 'CA':
        count += 2
        i += 2
        maxx = max(maxx, count)
    elif st[i - 1] + st[i] == 'CA' and st[i + 1] in 'CA':
        i += 1
        maxx = max(maxx, count + 1)
        count = 0
    else:
        i += 1
        count = 0
print(maxx)
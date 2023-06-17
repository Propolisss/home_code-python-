st = open('24_4113.txt').readline()
maxx = float('-inf')

for j in 0, 1:
    count = 0
    for i in range(j, len(st) - 1, 2):
        if st[i] + st[i + 1] in ['BB', 'DD']:
            count += 1
            maxx = max(maxx, count)
        else:
            count = 0
print(maxx)
st = open('24_4546.txt').readline().strip()
maxx = float('-inf')

for j in 0, 1, 2:
    count = 0
    for i in range(j, len(st) - 2, 3):
        if st[i] + st[i + 2] in ['AA', 'CC']:
            count += 1
            maxx = max(maxx, count)
        else:
            count = 0
print(maxx)
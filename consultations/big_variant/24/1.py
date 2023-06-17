st = open('24_7723.txt').readline().replace('R', 'D').replace('8', '1')
count = 0
maxx = float('-inf')

for j in 0, 1, 2:
    for i in range(j, len(st) - 2, 3):
        if st[i : i + 3] == '11D':
            count += 1
            maxx = max(maxx, count)
        else:
            count = 0
print(maxx)
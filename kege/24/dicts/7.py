st = open('24_2500.txt').readline()
count = 0

for i in range(len(st) - 3):
    if st[i] + st[i + 2: i + 4] == 'GME':
        count += 1
print(count)
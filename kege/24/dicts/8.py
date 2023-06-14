st = open('24_2501.txt').readline()
count = 0

for i in range(len(st) - 4):
    if st[i] + st[i + 2] + st[i + 4] == 'AAA':
        count += 1
print(count)
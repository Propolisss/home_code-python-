st = open('24_1143.txt').readline()
count = 0

for i in range(len(st) - 9):
    if st[i] + st[i + 6] == 'AF':
        count += 1
for i in range(len(st) - 7):
    if st[i] + st[i + 7] == 'AF':
        count += 1
for i in range(len(st) - 8):
    if st[i] + st[i + 8] == 'AF':
        count += 1
for i in range(len(st) - 9):
    if st[i] + st[i + 9] == 'AF':
        count += 1
print(count)
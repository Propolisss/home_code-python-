st = open('24_2499.txt').readline()
count = 0

for i in range(len(st) - 3):
    if st[i : i + 4] == 'XXXX':
        count += 1
print(count)